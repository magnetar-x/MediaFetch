import flet as ft
import yt_dlp
import time
import asyncio
import colorsys
import os

#Default Directory - Music
mf = os.path.join(os.path.expanduser('~'),'Music')
os.makedirs(mf, exist_ok=True)
os.chdir(mf)

#----------------------------
def aaditya(page: ft.Page):
    #Intro
    ft.title = "Media-Fetch"
    page.vertical_alignment = ft.MainAxisAlignment.START

    #Refresh Function
    def rfsh(e):
        l.opacity = 1
        b.disabled = False
        l2.visible = False
        l3.visible = False
        lbr.disabled = False
        pb.visible = False
        pb_text.visible = False
        frmt_indic.visible = False
        l1.value = "APP READY"
        l.value = ""
        l1.color = "#d4d101"
        page.update()

    #Theme toggle
    def tgl(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        tb.icon = ft.Icons.DARK_MODE if tb.icon == ft.Icons.SUNNY else ft.Icons.SUNNY
        tb.text = "DARK" if tb.text == "LIGHT" else "LIGHT"
        l.bgcolor = "#FCFCFC" if l.bgcolor == "#343433" else "#343433"
        l.color  = "#FCFCFC" if l.color == "#343433" else "#343433"
        lbr.bgcolor = "#FCFCFC" if lbr.bgcolor == "#343433" else "#343433"
        lbr.color  = "#FCFCFC" if lbr.color == "#343433" else "#343433"
        rb.bgcolor = "#CAE3F3" if rb.bgcolor == "#12181C" else "#12181C"
        page.update()

    #Keyboard event listener
    page.on_keyboard_event = shrt

    #Keyboard Shortcuts  
    def shrt(e : ft.KeyboardEvent):
        if ((e.key == 'T') & (e.ctrl == True)):
            tgl(e)
        elif((e.key == "R")&(e.ctrl == True)):
            rfsh(e)      

    #Progress Bar
    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total:
                percent = d.get('downloaded_bytes', 0) / total
                pb.value = percent
                pb_text.value = f"{percent:.1%}"
            else:
                pb.value = None
                pb_text.value = "Downloading..."
            page.update()
        elif d['status'] == 'finished':
            pb.value = 1.0
            pb_text.value = "Processing..."
            page.update()

    #Change in UI behaviour according to selected format
    def seg_change(e):
            if dd1.selected_index == 2 or dd1.selected_index == 3:
                lbr.disabled = True
            else:
                lbr.disabled = False
            lbr.update()
            dd1.update()

    #Directory picking
    def browse(e: ft.FilePickerResultEvent):
            os.chdir(f"{e.path}")

    #Download function
    def dld(e):
        #UI setup
        lbr.disabled = True
        l.opacity = 0.1
        b.disabled = True
        l1.value = "Downloading!"
        l1.color = "#9900aa"
        as1.content = cnt2
        pb.visible = True
        pb_text.visible = True
        pb.value = 0
        pb_text.value = "0%"
        page.update()
        page.update()
        a = l.value
        url = (a.partition("&"))[0]

        #Choice determination
        if dd1.selected_index == 0:
            dc = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'writethumbnail': True,
                'progress_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': f'{lbr.value}',
                },
                {
                    'key': 'EmbedThumbnail',
                }],
            }
        elif dd1.selected_index == 1:
            dc = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': '%(title)s.%(ext)s',
                'writethumbnail': True,
                'progress_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'EmbedThumbnail',
                }],
            }
        elif dd1.selected_index == 2:
                    dc = {
                        'format': 'bestvideo',
                        'outtmpl': '%(title)s.%(ext)s',
                        'writethumbnail': True,
                        'progress_hooks': [progress_hook],
                        'postprocessors': [{
                            'key': 'EmbedThumbnail',
                        }],
                    }
            
        try:
            with yt_dlp.YoutubeDL(dc) as ydl:
                dct = ydl.extract_info(url,download=True)
                global t,br
                t = dct.get('title')
        except:
            #in case of download error
            l3.value = "ERROR"
            l3.color = "#ff0000"
            l2.visible = True
            l3.visible = True
            as1.content = cnt3
            pb.visible = False
            page.update()
            time.sleep(1)
            l1.value = "Refreshing"
            l1.color = "#037eb7"
            as1.content = cnt4
            page.update()
            time.sleep(0.5)
            lbr.disabled = False
            l.opacity = 1
            b.disabled = False
            l1.value = "APP READY"
            l.value = ""
            l1.color = "#d4d101"
            as1.content = cnt1
            page.update()
            return
        
        l3.value = t
        l3.color = "#00bb00"
        l3.visible = True
        frmt_indic.visible = True
        if dd1.selected_index == 0:
            frmt = "MP3"
        elif dd1.selected_index == 1:
            frmt = "MP4"
        else :
            frmt = "Only Video"
        frmt_indic.value = frmt
        l2.visible = True
        l1.visible = True
        as1.content = cnt5
        b.disabled = False
        lbr.disabled = False
        l.opacity = 1
        pb.visible = False
        pb_text.visible = False
        page.update()

        time.sleep(3)
        l1.value = "Refreshing"
        l1.color = "#037eb7"
        as1.content = cnt4
        page.update()
        time.sleep(1.5)
        l.opacity = 1
        b.disabled = False
        l1.value = "APP READY"
        l.value = ""
        l1.color = "#d4d101"
        as1.content = cnt1
        page.update()

    #----------------------------------
    #Media fetch color cycle text
    ll = ft.Text(
                value="Media-Fetch", 
                 size=50, color="#e36e14",
                 weight=ft.FontWeight.BOLD
                 )

    #Cycle icons
    l0 = ft.Text(
                value="🎵🎧🎷🎸🎹🎺🎻🎶",
                size=25, 
                color="#f0c60c"
                )

    #Last downloaded text
    l2 = ft.Text(
                value="Last Download : ",
                size=30,
                color="#d36b03",
                visible=False
                )

    #Last downloaded item name
    l3 = ft.Text(
                value=" ",
                 size=30,
                 color="#00ff00",
                 visible=False
                 )

    #Error message
    frmt_indic = ft.Text(
                value=" ",
                 size=30,
                 color="#ff0080",
                 visible=False
                 )

    #Url entry box
    l = ft.TextField(width=500,
                height=50, 
                read_only=False, 
                border_color="#ff0000", 
                bgcolor="#343433", 
                color="#FCFCFC",
                label="Youtube URL",
                on_submit=dld,
                opacity=1,
                autofocus=True,
                prefix_icon=ft.Icons.LINK,
                border=ft.InputBorder.UNDERLINE
                )

    #Bit-rate box
    lbr = ft.TextField(
        value = 192,
        bgcolor="#343433", 
        color="#FCFCFC",
        label="Bitrate",
        border_color="#ff0000",
        width=80,
        text_align="center",
    )

    #Download Progress bar
    pb = ft.ProgressBar(
        width=400, 
        value=0, 
        visible=False, 
        color="#e36e14"
        )

    #Progress bar text
    pb_text = ft.Text(
        value="0%", 
        size=16, 
        visible=False)

    #App ready indicator
    l1 = ft.Text(
        value="APP READY", 
        size=30, 
        color="#d4d101"
        ) 

    #Download indicator
    l1dld = ft.Text(
        value="Downloading", 
        size=30, 
        color="#9900aa"
        )

    #Error Indicator
    l1err = ft.Text(
        value="ERROR", 
        size=30, 
        color="#ff0000"
        )

    #Refreshing Indicator
    l1rfrsh = ft.Text(
        value="Refreshing", 
        size=30, 
        color="#037eb7"
        )

    #Successful Download Indicator
    l1ds = ft.Text(
        value="Download Successful", 
        size=30, 
        color="#04d200"
        )

    #----------------------
    #Containers

    #App ready
    cnt1 = ft.Container(
        l1,
        alignment=ft.alignment.center,
        width=200,
        height=200
    )

    #Downloading
    cnt2 = ft.Container(
        l1dld,
        alignment=ft.alignment.center,
        width=200,
        height=200
    )

    #Error
    cnt3 = ft.Container(
        l1err,
        alignment=ft.alignment.center,
        width=200,
        height=200
    )

    #Refresh
    cnt4 = ft.Container(
        l1rfrsh,
        alignment=ft.alignment.center,
        width=200,
        height=200
    )

    #Successful Download
    cnt5 = ft.Container(
        l1ds,
        alignment=ft.alignment.center,
        width=400,
        height=400
    )

    #Format Switcher
    as1 = ft.AnimatedSwitcher(
        cnt1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    ) 

    #------------------------------
    
    #Async

    #Text color cycle
    async def colcyc():
        i = 0
        h = 0
        while True:
            r,g,b = colorsys.hsv_to_rgb(h, 1, 1)  
            r,g,b = int(r*255), int(g*255), int(b*255)
            ll.color = f"#{r:02x}{g:02x}{b:02x}"
            l.border_color = f"#{r:02x}{g:02x}{b:02x}"
            h+=0.005
            if h == 1:
                h = 0
            i += 1
            ll.update()
            l.update()
            await asyncio.sleep(0.05)

    #Icon cycle    
    async def txtcyc():
        msc = "🎵🎧🎷🎸🎹🎺🎻🎶"
        while True:
            l0.value = msc[-1] + msc[:-1]
            msc = msc[-1] + msc[:-1]
            l0.update()
            await asyncio.sleep(0.5)
            
    page.run_task(txtcyc)
    page.run_task(colcyc)

    #------------------------------------
    #Directory Browser
    fp = ft.FilePicker(on_result=browse)
    page.overlay.append(fp)
    dirb= ft.ElevatedButton(
            "Select Directory",icon=ft.Icons.FOLDER,
            on_click=lambda _: fp.get_directory_path()
        )

    #Format choice slider
    dd1 = ft.CupertinoSlidingSegmentedButton(
        selected_index=1,
        thumb_color=ft.Colors.RED_400,
        on_change=seg_change,
        controls=[
                    ft.Text("MP3"),
                    ft.Text("MP4"),
                    ft.Text("Only Video"),
                ],
    )

    #Theme Changer
    tb = ft.ElevatedButton(
        text="LIGHT",
        icon=ft.Icons.SUNNY, 
        on_click = tgl
        )
    
    #Downloader
    b = ft.ElevatedButton(
        text="Download", 
        icon=ft.Icons.MUSIC_NOTE, 
        on_click=dld)

    #Refresh
    rb = ft.FloatingActionButton(
        icon=ft.Icons.LOOP, 
        on_click=rfsh,mini=True,
        bgcolor="#12181C"
        )

    #-----------------------
    #Grid
    page.add(
        ft.Row([tb],alignment=ft.MainAxisAlignment.END),
        ft.Row([ll],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([l0], alignment=ft.MainAxisAlignment.CENTER,),
        ft.Row([l,lbr], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([pb, pb_text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([b,rb,dirb,dd1], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([l2,l3], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([frmt_indic], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([as1], alignment=ft.MainAxisAlignment.CENTER,height=150),
    )

ft.app(target = aaditya, view=ft.AppView.FLET_APP)