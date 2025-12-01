import flet as ft



def main(page: ft.Page):
	page.title = "Nota auxiliar"
	page.theme_mode = ft.ThemeMode.DARK
	#page.window.center()
	page.window.left= 40
	page.window.top= 750

	page.window.width=400
	page.window.height = 200
	page.window.resizable=True
	page.window.maximizable=False
	page.theme = ft.Theme(ft.Colors.DEEP_PURPLE_400)

	def on_keyboard(e: ft.KeyboardEvent):
		if( e.key=='Escape'):
			page.window.destroy()

	tTitulo= ft.Text(value="¡Nota rápida!", color="white")
	tinfo = ft.Text(value="Por: carlos@infocat", style=ft.TextThemeStyle.BODY_SMALL)
	mArea = ft.TextField(
		adaptive=True,
		label="Contenido de la nota",
		multiline=True,
		value="",
		min_lines=4,
		border_color = ft.Colors.AMBER_200,
		text_size=13
		)
	page.on_keyboard_event = on_keyboard
	page.controls.append(tTitulo)
	page.add(mArea, tinfo)
	mArea.focus()
	page.update()

ft.app(target=main, view=ft.AppView.FLET_APP)
