from playwright.sync_api import Page, expect

import pytest

from faker import Faker
fake = Faker()

@pytest.mark.webtable
def test_web_tables(page: Page):
    # 1️⃣ Datos dinámicos con Faker
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    age = str(fake.random_int(min=18, max=65))
    salary = str(fake.random_int(min=3000, max=15000))
    department = fake.job().split(" ")[0]  # toma la primera palabra del cargo

    # 2️⃣ Navegar a la página de Web Tables
    page.goto("https://demoqa.com/")
    page.get_by_text("Elements").click()
    page.get_by_text("Web Tables").click()

    # Esperar que la tabla sea visible
    expect(page.locator(".web-tables-wrapper")).to_be_visible()

    # 3️⃣ Crear un nuevo registro
    page.locator("#addNewRecordButton").click()
    page.fill("#firstName", first_name)
    page.fill("#lastName", last_name)
    page.fill("#userEmail", email)
    page.fill("#age", age)
    page.fill("#salary", salary)
    page.fill("#department", department)
    page.locator("#submit").click()

    # 4️⃣ Validar que el registro se muestra en la tabla
    page.fill("#searchBox", first_name)
    row = page.locator(".rt-tr-group").first
    expect(row).to_contain_text(first_name)
    expect(row).to_contain_text(last_name)
    expect(row).to_contain_text(email)
    expect(row).to_contain_text(department)

    # 5️⃣ Editar el registro
    row.locator("[title='Edit']").click()
    new_department = "QA"
    page.fill("#department", new_department)
    page.locator("#submit").click()

    # Confirmar que se actualizó
    page.fill("#searchBox", first_name)
    expect(page.locator(".rt-tr-group").first).to_contain_text(new_department)

    # 6️⃣ Eliminar el registro
    row = page.locator(".rt-tr-group").first
    row.locator("[title='Delete']").click()

    # Confirmar que ya no aparece
    page.fill("#searchBox", first_name)
    expect(page.locator(".rt-noData")).to_have_text("No rows found")

    page.pause()
