import dearpygui.dearpygui as dpg
import backend as bk

nums = []
buffer = 1
usr_ops = ['+','+','+','+']

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1280, height=720)

with dpg.font_registry():
    primary_font = dpg.add_font("/usr/share/fonts/gsfonts/NimbusMonoPS-Regular.otf",15)

dpg.set_global_font_scale(1.5)

def render_eqn():
    eqn_stuff = bk.gen_eqn(3,20,1)
    global nums
    nums = eqn_stuff[1]
    with dpg.window(label="",tag=12,width=800, height=300,pos=[30,60]):
        with dpg.group(horizontal=True,pos=[250,50]):
            tg = 20
            for i in range(len(nums)-1):
                dpg.add_text(str(nums[i]))
                if i < len(nums)-2:
                    dpg.add_combo(("+","-","*","/"),tag=tg,default_value="+",no_arrow_button=True,width=40,callback=user_eqn)
                    tg =tg+1
            equals_str = " = " + str(nums[len(nums)-1])
            dpg.add_text(equals_str)
        dpg.bind_font(primary_font)

def user_eqn(sender,value):
    global buffer
    eqn = ""
    global usr_ops
    usr_ops[sender-20] = value
    print(sender,value,nums,usr_ops)
    with dpg.window(tag=12,pos=[30,60],width=800,height=300):
        dpg.add_spacer()
        if buffer > 1:
            dpg.delete_item(31)
        buffer += 1
        with dpg.group(horizontal=True,pos=[250,100],tag=31):
            for i in range(len(nums)-2):
                eqn = eqn + str(nums[i]) + str(usr_ops[i])

            eqn += str(nums[len(nums)-2])
            eqn += ' = ' + str(nums[len(nums)-1])
            display = 'Your eqn is: ' + eqn
            dpg.add_text(display)
        
    

def callback_user_eqn(sender,value):
    print(sender,value)

def main():
    render_eqn()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

main()


