# UNDER PALE STREETLIGHTS

image flicker = Solid("#ffffff", xysize=(1920, 1080))  # White flash screen

transform flicker_effect:
    alpha 0.0
    linear 0.1 alpha 0.8
    linear 0.1 alpha 0.0
    pause 0.2
    linear 0.05 alpha 0.6
    linear 0.05 alpha 0.0



define an = Character("Anya", color = "#ffa8a3", who_bold=True)
define st = Character("Stranger", color = "#72c27c", who_bold=True)
define ira = Character("Ira", color = "#77d1ed", who_bold=True)
define ka = Character("Kaede", color = "#f78b25", who_bold=True)
define sasha = Character("Sasha", color = "#d61142", who_bold=True)
define vas = Character("Vasya", color = "#72c27c", who_bold=True)
define voice = Character("???", color = "#2c0d0d", who_bold=True)

default preferences.text_cps = 30

define gui.text_font = "fonts/SpecialElite-Regular.ttf"
define gui.name_text_font = "fonts/SpecialElite-Regular.ttf"
define gui.interface_text_font = "fonts/SpecialElite-Regular.ttf"

transform shake_text:
    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
    linear 0.03 xpos 0.48 ypos 0.52
    linear 0.03 xpos 0.52 ypos 0.48
    linear 0.03 xpos 0.50 ypos 0.50
    repeat


init python:
    def shaker(st, at):
        import random
        return 0.05, {
            "xpos": 0.5 + (random.random() - 0.5) * 0.01,
            "ypos": 0.5 + (random.random() - 0.5) * 0.01,
            "xanchor": 0.5,
            "yanchor": 0.5
        }

    shake_transform = DynamicDisplayable(shaker)


define slowdissolve = Dissolve(0.5)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 1.0
    yalign 1.0

transform left:
    xalign 0
    yalign 1.0

transform right:
    xalign 0.5
    yalign 1.0

define slowdissolve = Dissolve(1.0)



 
 
 
label start:
    define slowdissolve = Dissolve(1.0)
    play music "dementia.mp3" fadeout 1
 
    scene bg train
    with slowdissolve

    "The city outside the train window is a blur of lights and shadow. It's the kind of place where everyone has their secrets, and those secrets know each other well."
    "You don’t have a name here—not really. The city remembers you only as much as it needs to."

    show anya backpack at left 
    
    
    with slowdissolve

    an "New city ne§w me."

    "Anya’s words sound hollow, even to her. She knows the rhythm of starting fresh. But something about this place feels different—heavier."

    st "Hey, Ira is looking for a guitarist. She's in the club down the road(points at a neon light sign)"
    
    
    hide anya backpack
    with slowdissolve
    scene bg starryentrance
    with slowdissolve
    show stranger normal at slightright
    
    
    show anya backpack at left    
    an "Huh you talking to me? Who are you?"
    st "..."
    
    st "just a stranger, welcome"
    st "We will see each other if u don't get lost"
      
    hide stranger
    with slowdissolve

    "A strange encounter, but this city has a way of making everyone feel like they’ve known each other forever. Sometimes that’s just how it goes."
    
    an "Did he offer me that just by seeing my guitar case? Weird dude"
    an "I mean there's nothing bad if I go there right?"
    
    hide anya backpack
    with slowdissolve
    
    scene bg starry
    with slowdissolve
    
    show ira talking at left
    with slowdissolve
    ira "Hey your name is Anya, right?"
    ira "Nice to meet you, im Ira"
    
    show anya bpleft at slightright
    with slowdissolve
    an "How you know my name?"

    ira "The city tells us.."
    ira "We know everyone in the city"
    ira "By your case I can tell u play guitar"
    ira "You are here just in time, I was looking for a guitarist for this band"
    ira "Wanna try and show me what u can do?"
    
    an "Alright? I guess it won't hurt"
    
    ira "Nice! Then go on stage and set everything up. I will be right back with other band members"
    
    hide anya bpleft at slightright
    with slowdissolve
    
    hide ira talking at slightright
    with slowdissolve
    
    ira "i brought them!"
    
    ka " OH MY! Hello! Im Kaede, i play drums. And whats your name??"
    show kaede normal at left
    with slowdissolve

    an "Oh hey! Im Anya, nice to meet you. I play lead guitar"
    ka "so cool!! Oh look others are here"
    hide kaede normal at left
    with slowdissolve

    sasha "Yo im Sasha, i play bass"
    show sasha normal at left
    with slowdissolve
    
    vas "Im Vasya, rythm guitar"
    show vasya normal at slightright

    "Each of them introduces themselves, but it feels more like they are just pieces of something larger. Like they are part of the city, not just the band."
    "Anya wonders briefly if they even know who they are, or if it’s the city that tells them who they should be."
    
    an "thats so nice to meet you all"
    an "well you are just in time, let me show what i can play!!"
    
    hide sasha normal at left
    with slowdissolve
    
    hide vasya normal at left
    with slowdissolve
    
    scene bg anyasetup 
    with slowdissolve

    ira "Alright Anya, u can start."
 
    an "(Anya playing)"
    scene bg starry
    with slowdissolve
    
    show ira talking at left
    with slowdissolve
    ira "well, you are definetly not bad. You need more emotions though"
    ira "the city likes when you play at your maximum"
    "Maximum. The city has a way of demanding everything from you, even if you don’t want to give it. And it knows when you’re holding back."

    an "what are these stupid stories about the city? Why everyone talks about it like that"
    
    show kaede normal at slightright
    with slowdissolve
    
    ka "you havent seen it at night. Theres a lot of places where you can either get lost or find yourself" 
    "Lost or found. Anya isn’t sure which she fears more."
    
    an "got it, gonna be more careful from now on"
    ira "alright, thats it for today."
    ira "in two weeks we have a concert here. Rehearsals 4 times a week."
    ira "Im gonna text you, dont get late"
    an "sounds good"
    
    scene bg starryentrance
    with slowdissolve
    
    show anya backpack at left
    with slowdissolve
    
    an "(After few rehearsals i feel like the band gets more weird every day)"
    an "(The vibe getting worse in general for some reason, not only in the group)"
    an "huu at least getting along with Sasha"

    "The tension in the air grows thick. Anya can feel it, but it’s hard to pinpoint exactly when things started to feel wrong."
    "Maybe it’s the way Sasha's smiles seem a little too sharp now, or the way Ira watches her with a certain... expectation." 
    
    hide anya backpack
    with slowdissolve
    
    sasha "hey anya, excited for the rehearsal??"
    show sasha normal at left
    with slowdissolve

    show anya bpleft at slightright
    with slowdissolve
    an "oh hi. Kind of, at least ur here this time.."
    
    sasha "well anyway, lets go."
    an "yeah"
    an "you know what im excited for?"

    sasha "the concert yeah? Me too"

    an "do you also feel like the band cant really, uhhh, connect? You know what i mean?"
    sasha "yeah, except for us though, i feel like vasya can be real annoying sometimes"
    an "and i think ira is a bit too strict sometimes..."

    hide anya bpleft
    with slowdissolve

    hide sasha normal
    with slowdissolve

    scene bg proberoom
    with slowdissolve

    ira "hey guys, nice to see you"
    show ira talking at left
    ira "lets get ready for rehearsal, the earlier the better"
    ira "everyone present? Good"
    ira "That concert is our first and probably the only chance we got. Lets not fuck it up Anya"
    show anya talkingleft at slightright
    an "right, how should we play it though?"
    ira "just feel the song, and play at your maximum emotions"
    ka "its okay ann!! Just be yourself"
    an "lets do it then!"
    
    hide ira talking
    with slowdissolve
    
    hide anya talkingleft
    with slowdissolve

    scene bg starryentrance
    with slowdissolve

    show sasha normal at left
    with slowdissolve

    sasha "hey Anya, u played very nice today. The city must like you now."
    
    show anya bpleft at slightright 
    with slowdissolve

    an "thank you, you werent too bad yourself"
    sasha "uhm thanks, you know i wanted to ask you something"
    an "what is it?"
    sasha "do you wanna go outside sometime together? I know a reallyy nice place."
    an "alright, write me when ur free"

    hide anya bpleft 
    with slowdissolve
    hide sasha normal 
    with slowdissolve
    
    scene bg starry
    with slowdissolve
    
    show anya talkingleft at slightright
    with slowdissolve 
    
    an "hey Sasha, how are you?"
    
    
    with slowdissolve
    
    sasha "*um hey Anya, sorry to ask you over the phone, but remember how i told u about a cool place?*"
    an "yeah, what about it??"
    sasha "*what about going there today*?"
    an "oh! I mean sure, why not"
    sasha "*nice, lets meet in two hours*"
    sasha "*ill send u the geolocation*"
    an "okay, thanks, looking for it!"

    hide anya talkingleft

    scene bg rotten
    with slowdissolve

    show anya backpack at left
    with slowdissolve
    an "(where is he?? This place feels real uncanny..)"
    sasha "yo anya! Im here"

    hide anya backpack
    with slowdissolve


    show anya bpleft at slightright
    with slowdissolve


    show sasha normal at left
    with slowdissolve
    
    an "o hey sasha!"
    an "what is this place? Its so creepy"
    sasha "oh dont worry about it, its just a abandonded fabric"
    sasha "Ive been here like a million times so"
    an "okay? Lets go explore a bit "
    sasha "ill go take a smoke real quick tho"
    an "what?? didnt u say u quit last week??"
    sasha "I say i quit every week.."

    an "just go dog"
    sasha "okay, be right back"
    
    hide sasha normal

    with slowdissolve

    an "(im really worried about him sometimes..)"
    an "huh? Whats that??"

    
    
    label abandoned_place:

    scene bg cassette
    with slowdissolve
    "The place is empty except for the sound of distant wind and creaking metal. Sasha heads off to have a smoke, leaving Anya alone with the cassette."

    "She looks at the tape, then at the old, worn cassette player beside it. It doesn't look like it works anymore. Still, curiosity wins out."

    "Anya presses play. The tape crackles to life before she can even finish her thought."

    window hide
    show text "The city hums its own song. If you can’t hear it, you are safe. If you play along, it will listen. If you stop, so will your name." at shake_text
    pause 4
    hide text
    window show

    "The static echoes for a moment longer, then falls silent."

    "Anya looks around, feeling the weight of the silence. The tape doesn't seem to have a player... and yet, it played. She shivers slightly."

    menu:
        "Leave the cassette where it is.":
            "Anya sets the tape back down, her hands trembling slightly as she feels an inexplicable urge to move away."
        
        "Throw the cassette away.":
            "She stands up and tosses the cassette into a pile of trash, but somehow, it feels as if the city is watching her. The tape doesn’t seem gone at all."

    "Sasha returns, and the moment passes—except the strange sense of unease lingers with Anya."

    sasha "Hey Anya, its been like an hour already!! Lets go to the rehearsal already! Concert is in few hours.."
    an "uhm.. okay"


    label scene_5:
    scene bg starry
    with slowdissolve

    "The club is buzzing with anticipation. The sound of instruments being tuned fills the air as the band prepares for their first live performance. Anya walks into the familiar scene, her nerves just under the surface, trying to stay calm."
    with slowdissolve


    ira "You’re not late. Are you alright?"
    show ira talking at left
    with slowdissolve
    
    show anya talkingleft at slightright
    an "Mostly, let's begin."
    
    ira "Good. Let's do this. We can't afford to slack off."
    "Ira’s voice is steady, her determination clear. It's the final stretch, and everyone knows what's at stake."
    
    menu:
        "Focus on the performance":
            $ focus_on_performance = True
            an "I need to be focused. This is important."
            jump performance_focus

        "Think about the city":
            $ focus_on_performance = False
            an "I can’t stop thinking about the city... but I’ll push through."
            jump performance_focus

label performance_focus:
    # This is where the performance preparation happens, depending on the player's choice.
    if focus_on_performance:
        an "I’m in the zone. Nothing can stop me now."
        "Anya takes a deep breath, pushing all her distractions aside. Her mind sharpens, ready for what’s next."
    else:
        "A part of Anya’s mind drifts away to thoughts of the city, but she tries to push those thoughts aside, focusing on the moment."
        an "I’m not fully here... but I’ll manage."

    
    "The group stands together. Tension and excitement hang in the air."
    
    ira "Alright. This is it. Our first show. Everyone ready?"
    ka "As ready as I’ll ever be."
    sasha "Let’s make sure they remember this night."

    "The lights dim. The crowd cheers. The band starts playing their first song. The sound is tight, raw, emotional."
    "The music echoes through the venue. For a moment, everything feels perfect."



label concert_flicker:

    an "Okay... Let's do this."

    "The band begins to play. The crowd cheers."

    show flicker at flicker_effect
    "Suddenly, the lights flicker once."

    pause 0.5

    show flicker at flicker_effect
    "Then again, stronger. The crowd's faces blur in the strobe."

    sasha "Was that the lights?"

    ira "Keep playing!"

    show flicker at flicker_effect
    pause 0.4
    show flicker at flicker_effect
    pause 0.2

    an "No… something’s wrong."

    "The stage lights dim again, then snap back... but the crowd seems different. Their faces—are they even moving?"

    scene bg distorted_crowd 
    with slowdissolve

    an "Guys... do you see that?"
    ira "What the hell is happening to the audience?"
    ka "They’re just... standing there. Not cheering. Not blinking."

    "And then the sound distorts. Your instruments wail, off-key. Your own fingers won’t obey."

    vas "It’s the city again, isn’t it?"

    an "...We have to stop. We can’t play like this."

    ira "No. We finish this. Or we find out what’s doing this."

    menu:
        "Keep playing through the distortion":
            jump play_through
        "Stop and investigate":
            jump investigate

    label play_through:
    narrator "You try to push through. You scream your soul into the chords—but the lights go out completely. You’re left in darkness."

    jump city_absorbs_them

    label investigate:
    narrator "You drop your guitar. Ira nods. The band rushes off stage, into the back, toward the alley where the distortion feels strongest."

    jump investigate_path



label city_absorbs_them:

    ka "Did... we do it? Was that enough?"

    ira "I think so. It felt right. Like they were listening."

    sasha "They're gone... the souls. They disappeared when we played the last note."

    vas "Then why does it feel like we're still being watched?"

    an "…do you hear that?"


    ira "Anya?"

    an "The club walls... they’re moving."

    voice "You played well. So very well."

    ka "Was that... the city?"

    ira "This isn't right. We need to go."

    vas "We're not going anywhere."

    an "I think... we were never meant to leave."

    show flicker at flicker_effect
    pause 0.2
    show flicker at flicker_effect
    pause 0.1
    show flicker at flicker_effect
    pause 0.2

    sasha "It’s pulling us in—!"

    voice "Your music woke the city. And now it wants you..."

    ira "No! We gave it everything! This wasn’t the deal!"

    voice "There was no deal. Only hunger."

    ka "I don’t want to disappear!"

    an "It’s too late."

    scene bg black with slowdissolve
    pause 1.5
    
    "The city claimed them. Not out of malice, but hunger. A silence follows, deeper than before."
    "And somewhere, underground, echoes of their final song linger — forever unfinished."
    "Worst Ending - CITY ABSORBTION 1/2"

    jump credits



label investigate_path:

    an "We need to know what this place did to our sound. I’m not letting it end like that."

    ira "Then we search. There was that old club... it might be connected."

    sasha "You sure? It’s condemned."

    vas "Exactly. That’s where the noise wants us."

    "The group heads into the heart of the city. To the place where sound began to rot."

    # Choice 2 - Deeper path
    menu:
        "Take it seriously and stick together":
            jump happy_ending
        "Argue and split up":
            jump band_falls_apart





label happy_ending:

    scene bg abandoned_club_night with slowdissolve
    play music "eerie_echoes.ogg" fadein 2.0

    "Inside the dusty, hollow club, they found rows of seats..."

    "Filled with unmoving shadows. Faint faces. Lost souls."

    ka "Are they... listening?"

    sasha "They’ve been waiting."

    vas "On the stage... instruments."

    an "They're not ours, but..."

    ira "We know what to do."

    "Without a word, they picked up the instruments. As if drawn by something ancient. Sacred."



    an "Let’s give them what they lost."

    play music "for game.ogg" fadein 2.0

    scene bg abandonded_club_onstage
    with slowdissolve

    "And so they played. A song of memory, regret, and hope."

    "One by one, the souls began to shimmer... until only the silence remained."

    ira "We did it."

    sasha "I feel... free."

    "They walked home under the morning sky. Together."

    "Best Ending - CONCERT FOR INHUMAN 2/2"
    "PS pls stay for a bit and listen to the song the band is playing on stage, cuz i wrote it myself and it took hella time"

    jump credits

    return

label band_falls_apart:

    scene bg abandoned_club_night with slowdissolve


    narrator "The club welcomed them with cold shadows in every seat."

    narrator "Dozens of lost souls stared, silent. Expectant."

    ka "Why are we even here?"

    ira "To play. To fix this."

    sasha "We can't fix anything anymore."

    vas "This was a mistake."

    "The instruments waited on stage. Untouched. Unplayed."

    an "Please... can we just try—"

    ka "No. I’m done."

    "And like that, the music died before it began."

    "The souls remained. So did the silence."

    an "…do you hear that?"


    ira "Anya?"

    an "The club walls... they’re moving."

    voice "You played well. So very well."

    ka "Was that... the city?"

    ira "This isn't right. We need to go."

    vas "We're not going anywhere."

    an "I think... we were never meant to leave."

    show flicker at flicker_effect
    pause 0.2
    show flicker at flicker_effect
    pause 0.1
    show flicker at flicker_effect
    pause 0.2

    sasha "It’s pulling us in—!"

    voice "Your music woke the city. And now it wants you..."

    ira "No! We gave it everything! This wasn’t the deal!"

    voice "There was no deal. Only hunger."

    ka "I don’t want to disappear!"

    an "It’s too late."

    scene bg black with slowdissolve
    pause 1.5
    
    "The city claimed them. Not out of malice, but hunger. A silence follows, deeper than before."
    "And somewhere, underground, echoes of their final song linger — forever unfinished."
    "Worst Ending - CITY ABSORBTION 1/2"

    jump credits


label credits:

    window hide

    scene bg black with slowdissolve
    pause 1

    show text "Special thanks to everyone who supported me during the making of this game." at truecenter
    with slowdissolve
    pause 4

    show text "Made with love using Ren'Py. :)" at truecenter
    with slowdissolve
    pause 4

    show text "This game is dedicated to those who have a big passion for writing music, playing music, or simply dreaming of it. For those who feel the rhythm in their soul and express it through every note they play." at truecenter
    with slowdissolve
    pause 5

    show text "If you ever dream of performing on stage, never give up. You have that spark in your eyes, and your passion will light the way." at truecenter
    with slowdissolve
    pause 5

    show text "Keep going, keep dreaming, and never stop believing." at truecenter
    with slowdissolve
    pause 4

    show text "The stage is waiting for us." at truecenter
    with slowdissolve
    pause 4


    show text "Game by Nikita Kucher" at truecenter
    with slowdissolve
    pause 4

    return











