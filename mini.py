import flet as ft



def main(page: ft.Page):
	page.window_center()
	page.window_width=400
	page.window_height = 180
	page.window_resizable=True
	page.window_maximizable=False
	page.theme_mode = ft.ThemeMode.DARK
	page.theme = ft.Theme(ft.colors.ORANGE_200)

	def on_keyboard(e: ft.KeyboardEvent):
		if( e.key=='Escape'):
			page.window_destroy()

	t = ft.Text(value="¡Nota rápida!", color="white")
	mt = ft.TextField(
		label="Contenido de la nota",
		multiline=True,
		value="",
		min_lines=3,
		border_color = ft.colors.AMBER_200
		)
	page.on_keyboard_event = on_keyboard
	page.controls.append(t)
	page.add(mt)
	page.update()

ft.app(target=main)
