# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def launch_browser():
    """Lanza el navegador visible y maximizado."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--start-maximized",       # Maximiza la ventana
                "--window-size=1920,1080"  # Fuerza tamaño completo
            ]
        )
        yield browser
        browser.close()

@pytest.fixture()
def page(launch_browser):
    """Crea una nueva página con viewport igual al tamaño de la ventana."""
    context = launch_browser.new_context(
        viewport={"width": 1920, "height": 1080},  # Ocupa toda la pantalla
        storage_state = "tests/login/storage_state.json"  # 🔥 Usa sesión guardada
    )
    page = context.new_page()
    yield page
    context.close()
