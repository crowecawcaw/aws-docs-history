import unittest
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup

from crawler import (
    build_local_image_path,
    IMAGE_PATH_PREFIX,
    looks_like_api_doc,
    looks_like_non_service,
    url_to_output_path,
    extract_main_content,
    convert_html_to_markdown,
    LinkChecker,
)


class TestImagePaths(unittest.TestCase):
    """Test image path building functionality."""

    def test_build_local_image_path_places_asset_within_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "docs"
            image_path = "/images/deadline-cloud/latest/userguide/images/monitor-job-status.png"

            local_path = build_local_image_path(image_path, output_root)

            expected = output_root / "deadline-cloud/latest/userguide/images/monitor-job-status.png"
            self.assertEqual(local_path, expected)

    def test_build_local_image_path_rejects_missing_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                build_local_image_path("/assets/example.png", Path(tmp))

    def test_build_local_image_path_ignores_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            image_path = f"{IMAGE_PATH_PREFIX}../deadline-cloud/./latest/userguide/images/example.png"

            local_path = build_local_image_path(image_path, Path(tmp))

            expected = Path(tmp) / "deadline-cloud/latest/userguide/images/example.png"
            self.assertEqual(local_path, expected)


class TestServiceFiltering(unittest.TestCase):
    """Test service and guide filtering functionality."""

    def test_looks_like_api_doc_detects_api_references(self):
        # Should detect API references
        self.assertTrue(looks_like_api_doc("APIReference"))
        self.assertTrue(looks_like_api_doc("api-reference"))
        self.assertTrue(looks_like_api_doc("apiref"))
        self.assertTrue(looks_like_api_doc("latest-api"))

        # Should not detect user guides
        self.assertFalse(looks_like_api_doc("userguide"))
        self.assertFalse(looks_like_api_doc("developerguide"))
        self.assertFalse(looks_like_api_doc("latest"))

    def test_looks_like_non_service_detects_sdks(self):
        # Should detect SDKs
        self.assertTrue(looks_like_non_service("sdk-for-python"))
        self.assertTrue(looks_like_non_service("sdk-for-java"))
        self.assertTrue(looks_like_non_service("python3"))
        self.assertTrue(looks_like_non_service("powershell"))
        self.assertTrue(looks_like_non_service("aws-toolkit"))

        # Should not detect actual services
        self.assertFalse(looks_like_non_service("s3"))
        self.assertFalse(looks_like_non_service("ec2"))
        self.assertFalse(looks_like_non_service("deadline-cloud"))


class TestUrlToOutputPath(unittest.TestCase):
    """Test URL to output path conversion."""

    def test_url_to_output_path_basic(self):
        url = "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html"
        output_root = Path("/tmp/docs")

        result = url_to_output_path(url, output_root)

        expected = output_root / "deadline-cloud/latest/userguide/what-is-deadline-cloud.md"
        self.assertEqual(result, expected)

    def test_url_to_output_path_index(self):
        url = "https://docs.aws.amazon.com/s3/latest/userguide/"
        output_root = Path("/tmp/docs")

        result = url_to_output_path(url, output_root)

        expected = output_root / "s3/latest/userguide.md"
        self.assertEqual(result, expected)

    def test_url_to_output_path_removes_html_extension(self):
        url = "https://docs.aws.amazon.com/ec2/latest/userguide/concepts.html"

        result = url_to_output_path(url)

        expected = Path("ec2/latest/userguide/concepts.md")
        self.assertEqual(result, expected)


class TestHtmlToMarkdownConversion(unittest.TestCase):
    """Test HTML to Markdown conversion with real AWS documentation patterns."""

    def test_extract_main_content_finds_awsdocs_content(self):
        html = """
        <html>
            <head><title>Test</title></head>
            <body>
                <nav>Navigation</nav>
                <div id="awsdocs-content">
                    <h1>Main Content</h1>
                    <p>This is the documentation.</p>
                </div>
                <footer>Footer</footer>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")

        main = extract_main_content(soup)

        self.assertIn("Main Content", main.get_text())
        self.assertNotIn("Navigation", main.get_text())

    def test_convert_html_to_markdown_preserves_structure(self):
        html = """
        <h1>Amazon S3 Overview</h1>
        <p>Amazon Simple Storage Service (Amazon S3) is an object storage service.</p>
        <h2>Key Features</h2>
        <ul>
            <li>Durability</li>
            <li>Scalability</li>
            <li>Security</li>
        </ul>
        <pre><code>aws s3 cp myfile.txt s3://mybucket/</code></pre>
        """

        markdown = convert_html_to_markdown(html)

        self.assertIn("# Amazon S3 Overview", markdown)
        self.assertIn("## Key Features", markdown)
        self.assertIn("* Durability", markdown)
        self.assertIn("* Scalability", markdown)
        self.assertIn("```", markdown)
        self.assertIn("aws s3 cp myfile.txt s3://mybucket/", markdown)

    def test_convert_html_to_markdown_handles_tables(self):
        html = """
        <table>
            <tr><th>Service</th><th>Use Case</th></tr>
            <tr><td>S3</td><td>Object storage</td></tr>
            <tr><td>EC2</td><td>Compute instances</td></tr>
        </table>
        """

        markdown = convert_html_to_markdown(html)

        self.assertIn("|", markdown)
        self.assertIn("Service", markdown)
        self.assertIn("S3", markdown)
        self.assertIn("Object storage", markdown)


class TestLinkChecker(unittest.TestCase):
    """Test URL link checking and filtering."""

    def test_link_checker_accepts_valid_docs_urls(self):
        checker = LinkChecker(allowed_prefixes=["/s3/latest/userguide/"])

        valid_urls = [
            "https://docs.aws.amazon.com/s3/latest/userguide/index.html",
            "https://docs.aws.amazon.com/s3/latest/userguide/getting-started.html",
            "https://docs.aws.amazon.com/s3/latest/userguide/",
        ]

        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(checker(url))

    def test_link_checker_rejects_images_and_pdfs(self):
        checker = LinkChecker()

        invalid_urls = [
            "https://docs.aws.amazon.com/images/example.png",
            "https://docs.aws.amazon.com/pdfs/s3/whitepaper.pdf",
            "https://docs.aws.amazon.com/assets/logo.svg",
        ]

        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(checker(url))

    def test_link_checker_rejects_external_domains(self):
        checker = LinkChecker()

        external_urls = [
            "https://aws.amazon.com/s3/",
            "https://console.aws.amazon.com/s3/",
            "https://github.com/aws/aws-cli",
        ]

        for url in external_urls:
            with self.subTest(url=url):
                self.assertFalse(checker(url))

    def test_link_checker_respects_allowed_prefixes(self):
        checker = LinkChecker(allowed_prefixes=["/s3/latest/userguide/"])

        # Should accept URLs with the allowed prefix
        self.assertTrue(checker("https://docs.aws.amazon.com/s3/latest/userguide/index.html"))

        # Should reject URLs without the allowed prefix
        self.assertFalse(checker("https://docs.aws.amazon.com/ec2/latest/userguide/index.html"))


if __name__ == "__main__":
    unittest.main()
