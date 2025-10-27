from playwright.sync_api import sync_playwright

def save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.saucedemo.com/v1/")

        # Completa el login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Espera a que cargue el inventario (indicador de login exitoso)
        page.wait_for_url("**/inventory.html")

        # Guarda el estado de la sesión
        context.storage_state(path="storage_state.json")

        print("✅ Sesión guardada en 'storage_state.json'")

        browser.close()

if __name__ == "__main__":
    save_login_state()
