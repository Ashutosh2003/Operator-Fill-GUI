import dearpygui.dearpygui as dpg
import backend as bk

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1280, height=720)

with dpg.font_registry():
    primary_font = dpg.add_font("/usr/share/fonts/gsfonts/NimbusMonoPS-Regular.otf",15)

dpg.set_global_font_scale(1.5)

def render_eqn():
    eqn = bk.gen_eqn(3,20,1)
    with dpg.window(label="",tag=12,width=640, height=200):
        with dpg.group(horizontal=True,pos=[250,50]):
            for _ in range(5):
                dpg.add_text("4")
                dpg.add_combo(("+","-","*","/"),default_value="+",no_arrow_button=True,width=40)

        dpg.bind_font(primary_font)

def main():
    render_eqn()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

main()


