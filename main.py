import flet as ft
tasks = []
def add (newtaskfun, page):
    page.add(ft.Checkbox(label=newtaskfun.value))


def edit (editnumberfun,edittaskfun,page):
    tasks.insert(editnumberfun, edittaskfun)


def delete (deletenumberfun,page):
    tasks.pop(deletenumberfun)
def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=tasks.value))
        tasks.value = ""
        tasks.focus()
        tasks.update()

        task = ft.TextField(hint_text="Какая новая задача?", width=300)
        page.add(ft.ElevatedButton(text="Добавить", on_click=add(task)))

        editnumber = ft.TextField(hint_text="Номер задачи для изменеия?", width=300)
        edittask = ft.TextField(hint_text="Новый текст задачи?", width=300)
        page.add(ft.ElevatedButton(text="Изменить", on_click=edit(editnumber,edittask)))

        deletenumber = ft.TextField(hint_text="Что нужно удалить?", width=300)
        page.add(ft.ElevatedButton(text="Удалить", on_click=delete(deletenumber)))



ft.app(main)
