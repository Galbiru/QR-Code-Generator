from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Load the page
    page.goto('file:///app/index.html')

    # Test 1: Verify Title and default elements
    print("Checking page title...")
    assert "QR Code Master" in page.title()

    # Test 2: Check for Color Inputs
    print("Checking color inputs...")
    assert page.is_visible('#colorDark')
    assert page.is_visible('#colorLight')

    # Test 3: Change color and generate QR (Text mode)
    print("Testing generation with custom colors...")
    page.fill('#inputText', 'Color Test')

    # Change colors
    # Use fill for color inputs
    page.fill('#colorDark', '#ff0000') # Red
    page.fill('#colorLight', '#000000') # Black

    page.click('button.action-btn')

    # Wait for canvas
    page.wait_for_selector('canvas')

    # Check if canvas exists
    canvas = page.query_selector('canvas')
    assert canvas is not None

    # Take screenshot
    page.screenshot(path='/home/jules/verification/color_mode.png')
    print("Screenshot saved to /home/jules/verification/color_mode.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
