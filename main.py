import streamlit as st
import utils.basic as t
# t.set_ph(1)
# Start
lines = [
    "Hey?",
    "Wake up",
    "The time isn't right yet",
    "Emm...",
    "Can I know more about you?",
    "Emm... okay",
    "6YKj576k572R5pq06ICF5b6I6K6o5Y6M77yM5LiN5piv5ZCX77yf",
    "QmJsMTUtQW50YWdvbmlzbXPvvIzkuI3opoHnkIbkvJrku5bku6zvvIzotbDlpb3oh6rlt7HnmoTot6/vvIE=",
    "572R5pq0NOmprO+8jOe9keaatOaIkeiNieazpemprO+8jOaIkeiNieatu+S9oOWFqOWutu+8jOaIkeWOu+S9oOWmiOeahOmalOWjgeeahOWPuOmprOWCu+mAvO+8jOS9oOS7rOS4jemFjea0u+edgO+8jOaZi+acneS6uuWPuOmprOWutu+8jOi/meS5iOivtOmDveS7luWmiOS+rui+sei/meS6m+ivje+8jOaIkeS7luWmiOS7peWQjuWGjeS5n+WmiOeahOmalOWjgeeahOeUqOS4jeS6hui/meS6m+ivjeS6huWlveS4jeWlve+8jOaTjeS9oOWmiOeahOWCu+mAvA=="
]

code = f"""
<h1><center><div id="type_box" style="color:white"></div></center></h1>
<script>
const lines = {lines};
const el = document.getElementById("type_box");
let lineIdx = 0;
let charIdx = 0;

function type(){{
    if(lineIdx >= lines.length) return;
    const curLine = lines[lineIdx];
    if(charIdx < curLine.length){{
        el.innerText = curLine.substring(0, charIdx+1);
        charIdx++;
        setTimeout(type,80);
    }}else{{
        setTimeout(()=>{{
            lineIdx++;
            charIdx = 0;
            type();
        }},1000);
    }}
}}
type();
</script>
"""
st.components.v1.html(code, height = 220)
