# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    Fills in two numbers, clicks the "Add" button, and verifies the displayed result.
    Waits for the result to appear to avoid timing issues.
    """
    page.goto('http://localhost:8000')

    # Fill the input fields
    page.fill('#a', '10')
    page.fill('#b', '5')

    # Click "Add"
    page.click('button:text("Add")')

    # Wait for the result div to contain text
    page.wait_for_selector('#result')

    # Check the result
    result_text = page.inner_text('#result').strip()
    assert result_text == 'Result: 15', f"Expected 'Result: 15', got '{result_text}'"


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    Waits for the result div to ensure the error message is rendered.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '10')
    page.fill('#b', '0')

    page.click('button:text("Divide")')

    # Wait for the result element to appear
    page.wait_for_selector('#result')

    # Get the result text and strip whitespace
    result_text = page.inner_text('#result').strip()
    
    # Assert the correct error message
    assert result_text == 'Error: Cannot divide by zero!', f"Expected 'Error: Cannot divide by zero!', got '{result_text}'"

