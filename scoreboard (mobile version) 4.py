#scoreboard


from tkinter import *
import time


#defining program variables

root_geometry='300x190'

max_points=21
blue_score=0 #player 1
red_score=0 #player 2

button_width=15
button_height=2
button_borderwidth=3
button_width_small=2
total_score=0
serve_counter=''
serial=0
var='active' #active or passive
game_length='full' #full or half
who_serve='Blue'
game_status='Started'

#defining all the colours
deep_blue='#1b4887'
deep_red='#910f0f'
just_white='#ffffff'
just_yellow='#ffd56b'
just_silver='#f0f0f0'

#text type
text_font=('Ariel', 20)


#defining the properties of root window
root=Tk()
root.title('Scoreboard')
root.geometry(root_geometry)




#will host pack function 
canvas1=Canvas(root)
canvas1.pack()

#will host grid function
canvas2=Canvas(root)
canvas2.pack()

#will host auxilary buttons
canvas3=Canvas(root)
canvas3.pack()


#blank command for experimental purposes
def nocommand():
    pass



def blue_plus():
    
    global var
    global who_serve
    global game_status
    global serve_counter

    game_status='Running'


    if var=='active':

        global blue_score
        blue_score+=1
        blue_label.config(text=blue_score)

        global total_score
        total_score+=1
        serve_counter=(str(total_score))[-1]

        if serve_counter=='0' or serve_counter=='1' or serve_counter=='2' or serve_counter=='3' or serve_counter=='4':

            who_serve='Blue'

            blue_label.config(bg=just_yellow)
            red_label.config(bg=just_silver)

        else:

            if True: #old statement

                who_serve='Red'

                blue_label.config(bg=just_silver)
                red_label.config(bg=just_yellow)

            else:
                pass

                '''
                who_serve='not available'

                blue_label.config(bg=just_silver)
                red_label.config(bg=just_silver)
                '''

        label_total_score.config(text=total_score)

    elif var=='passive':
        pass


    if game_length=='full':
        if blue_score>=21 and blue_score-red_score>=2:
            label_total_score.config(text='Blue wins')
            var='passive'
            game_status='Blue wins'

        else:
            pass

    elif game_length=='half':
        if blue_score>=11 and blue_score-red_score>=2:
            label_total_score.config(text='Blue wins')
            var='passive'
            game_status='Blue wins'

        else:
            pass

    else:
        label_total_score.config(text='Game length ERROR!')
        game_status='Encountered an unexpected error'
        



def blue_minus():

    global blue_score
    global game_status

    if blue_score>0:
        blue_score-=1
        blue_label.config(text=blue_score)

        global total_score

        if total_score>0:
            total_score-=1
            label_total_score.config(text=total_score)

        else:
            total_score.config(text=total_score)

    else:
        pass

    global var
    var='active'
    game_status='Running'
















def red_plus():

    global var
    global who_serve
    global game_status
    global serve_counter

    game_status='Running'

    if var=='active':

        global red_score
        red_score+=1
        red_label.config(text=red_score)

        global total_score
        total_score+=1
        serve_counter=(str(total_score))[-1]

        if not(serve_counter=='5' or serve_counter=='6' or serve_counter=='7' or serve_counter=='8' or serve_counter=='9'):

            who_serve='Red'

            blue_label.config(bg=just_yellow)
            red_label.config(bg=just_silver)

        else:

            if True: #old statementtotal_score<100

                who_serve='Blue'

                blue_label.config(bg=just_silver)
                red_label.config(bg=just_yellow)

            else:
                pass

                '''
                blue_label.config(bg=just_silver)
                red_label.config(bg=just_silver)
                '''

        label_total_score.config(text=total_score)


    elif var=='passive':
        pass


    if game_length=='full':
        if red_score>=21 and red_score-blue_score>=2:
            label_total_score.config(text='Red wins')
            var='passive'
            game_status='Red wins'

        else:
            pass

    elif game_length=='half':
        if red_score>=11 and red_score-blue_score>=2:
            label_total_score.config(text='Red wins')
            var='passive'
            game_status='Red wins'

        else:
            pass

    else:
        label_total_score.config(text='Game length ERROR!')
        game_status='Encountered an unexpected error'



def red_minus():

    global red_score
    global game_status

    if red_score>0:
        red_score-=1
        red_label.config(text=red_score)

        global total_score

        if total_score>0:
            total_score-=1
            label_total_score.config(text=total_score)

        else:
            total_score.config(text=total_score)

    else:
        pass

    global var
    var='active'
    game_status='Running'




def reset():

    global blue_score
    global red_score
    global total_score
    global game_status

    blue_score=0
    red_score=0
    total_score=0

    blue_label.config(text=blue_score, bg=just_yellow)
    red_label.config(text=red_score, bg=just_silver)
    label_total_score.config(text=total_score)
    
    global var
    var='active'
    game_status='Started'



def save():

    time.sleep(2)


    #defining global variables
    global blue_score
    global red_score
    global total_score
    global serial

#------------------------------------------
    #serial number allocation
    srno=open('srno.txt', 'r')

    if srno.read()=='':

        temp=1

        srno=open('srno.txt', 'w')
        srno.write(str(temp))

        srno.close()


    else:

        srno=open('srno.txt', 'r')

        temp=int(srno.read())
        temp+=1

        srno=open('srno.txt', 'w')
        srno.write(str(temp))

        srno.close()

    srno.close()

#------------------------------------------
    #game length description
    if game_length=='half':
        game_length_type='Half'

    elif game_length=='full':
        game_length_type='Full'



#------------------------------------------
    #time description
    hour=str(time.strftime('%I'))
    minute=str(time.strftime('%M'))
    second=str(time.strftime('%S'))
    date=str(time.strftime('%d'))
    month=str(time.strftime('%m'))
    year=str(time.strftime('%y'))
    day=str(time.strftime('%a'))
    am_pm=str(time.strftime('%p'))

    cur_time=hour+':'+minute+':'+second+' '+am_pm
    cur_date=date+'/'+month+'/'+year+' '+day


#------------------------------------------
    #last game file
    last_game=open('last_game.txt', 'w')
    last_game.write('Blue score: '+(str(blue_score))+' | Red score: '+(str(red_score))+' | \n')
    last_game.write('Status: '+game_status+'\n')
    last_game.write('Game length: '+game_length_type+ '\n')
    last_game.write('Current serve: '+ who_serve+'\n')
    last_game.write('Recorded on: '+cur_time+'\n')
    last_game.write('On date: '+cur_date+'\n')

#------------------------------------------
    #file management
    file=open("Text_document.txt", "a")
    srno=open('srno.txt', 'r')

    file.write('Game number:'+srno.read()+'\n')
    file.write('Blue score: '+(str(blue_score))+' | Red score: '+(str(red_score))+' | \n')
    file.write('Status: '+game_status+'\n')
    file.write('Game length: '+game_length_type+ '\n')
    file.write('Current serve: '+ who_serve+'\n')
    file.write('Recorded on: '+cur_time+'\n')
    file.write('On date: '+cur_date+'\n')
    file.write('\n')
    file.write('-----------------------------\n')

    file.close()
    srno.close()











def full():
    
    global game_length
    game_length='full'
    full.config(bg='orange')
    half.config(bg='#f0f0f0')
    


def half():
    
    global game_length
    game_length='half'
    full.config(bg='#f0f0f0')
    half.config(bg='orange')




















label_title=Label(canvas1, text='Scoreboard')
label_title.pack()
#canvas1


label_total_score=Label(canvas1, text=total_score,font=text_font )
label_total_score.pack()




blue_label=Label(canvas2, text=blue_score, bg=just_yellow, font=text_font)
blue_label.grid(row=1, column=1)

blue_increase=Button(canvas2, text='Inc.', width=button_width, height=button_height, borderwidth=button_borderwidth, bg=deep_blue, fg=just_white, command=blue_plus)
blue_increase.grid(row=2, column=1)

blue_decrease=Button(canvas3, text='Dec.', width=button_width_small, height=button_height, borderwidth=button_borderwidth, command=blue_minus)
blue_decrease.grid(row=1, column=1)





red_label=Label(canvas2, text=red_score,font=text_font)
red_label.grid(row=1, column=2)

red_increase=Button(canvas2, text='Inc.', width=button_width, height=button_height, borderwidth=button_borderwidth, bg=deep_red, fg=just_white, command=red_plus)
red_increase.grid(row=2, column=2)


red_decrease=Button(canvas3, text='Dec.', width=button_width_small, height=button_height, borderwidth=button_borderwidth, command=red_minus)
red_decrease.grid(row=1, column=6)


reset=Button(canvas3, text='Res.', width=button_width_small, height=button_height, borderwidth=button_borderwidth, command=reset)
reset.grid(row=1, column=2)

save=Button(canvas3, text='Save', width=button_width_small, height=button_height, borderwidth=button_borderwidth, command=save)
save.grid(row=1, column=5)


#red_decrease=Button(canvas3, text='Dec.', width=button_width_small, height=button_height, borderwidth=button_borderwidth, command=red_minus)
#red_decrease.grid(row=3, column=3)

full=Button(canvas3, text='Full', width=button_width_small, height=button_height, borderwidth=button_borderwidth, bg='orange', command=full)
full.grid(row=1, column=3)


half=Button(canvas3, text='Half', width=button_width_small, height=button_height, borderwidth=button_borderwidth, bg='#f0f0f0', command=half)
half.grid(row=1, column=4)

root.mainloop()