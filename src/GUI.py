import dearpygui.dearpygui as dpg
import time
import backend as bk

WINDOW_X = 100
WINDOW_Y = 320

nums = []
buffer = False
usr_ops = ['+','+','+','+','+','+','+','+']
usr_eqn = ""
eqn_stuff = ""

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=300)

#with dpg.font_registry():
    #primary_font = dpg.add_font("NimbusMonoPS-Regular.otf",15)

dpg.set_global_font_scale(2)

def render_eqn():
    global eqn_stuff
    eqn_stuff = bk.gen_eqn(2,20,1)
    global nums
    nums = eqn_stuff[1]
    with dpg.window(label="",tag=12,width=800, height=300,pos=[WINDOW_X,WINDOW_Y]):
        with dpg.group(horizontal=True,pos=[250,50],tag=13):
            tg = 20
            for i in range(len(nums)-1):
                dpg.add_text(str(nums[i]))
                if i < len(nums)-2:
                    dpg.add_combo(("+","-","*","/"),tag=tg,default_value=" ",no_arrow_button=True,width=40,callback=user_eqn)
                    tg =tg+1
            equals_str = " = " + str(nums[len(nums)-1])
            dpg.add_text(equals_str)
        #dpg.bind_font(primary_font)


def user_eqn(sender,value):
    global buffer
    global usr_eqn
    global usr_ops
    usr_eqn = ""
    usr_ops[sender-20] = value
    print(sender,value,nums,usr_ops)
    with dpg.window(tag=12,pos=[WINDOW_X,WINDOW_Y],width=800,height=300):
        dpg.add_spacer()
        if buffer == True:
            dpg.delete_item(31)
        buffer = True
        with dpg.group(horizontal=True,pos=[250,100],tag=31):
            for i in range(len(nums)-2):
                usr_eqn = usr_eqn + str(nums[i]) + str(usr_ops[i])

            usr_eqn += str(nums[len(nums)-2])
            display_eqn = usr_eqn + ' = ' + str(nums[len(nums)-1])
            display = 'Your eqn is: ' + display_eqn
            dpg.add_text(display)


def render_buttons():
    with dpg.window(tag=12,pos=[WINDOW_X,WINDOW_Y],width=800,height=300):
        with dpg.group(horizontal=True,pos=[250,150],tag=32):
            #dpg.add_spacer()
            show_score = dpg.add_button(label='Exit and show score',tag=41)
            skip = dpg.add_button(label='skip', tag=42, callback=skip_callback)
            submit = dpg.add_button(label='submit',tag=43,callback=submit_callback,enabled=True)
        

def chck_ans(usr_inp,ans):
    usr_ans = round(eval(usr_inp),3)
    print(usr_ans)
    if usr_ans == ans:
        return True
    else:
        return False


def reset():
    global buffer
    dpg.delete_item(12)
    buffer=False
    render_eqn()
    render_buttons()


def submit_callback():
    global usr_eqn
    global nums
    if chck_ans(usr_eqn,nums[len(nums)-1]):
        with dpg.window(tag=12,pos=[WINDOW_X,WINDOW_Y]):
            dpg.delete_item(13)
            dpg.delete_item(31)
            dpg.add_text("Correct",pos=[30,60])
            time.sleep(2)
        reset()


def skip_callback():
    global eqn_stuff
    skip_text = 'An ans was ' + eqn_stuff[0]
    with dpg.window(tag=12,pos=[WINDOW_X,WINDOW_Y]):
            dpg.delete_item(13)
            if buffer == True:
                 dpg.delete_item(31)
            dpg.add_text(skip_text,pos=[250,60])
            time.sleep(6)
    reset()
        
            
        
def main():
    render_eqn()
    render_buttons()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

main()


