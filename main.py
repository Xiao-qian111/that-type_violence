import streamlit as st
import utils.basic as t
t.set_ph(1)
# Start
lines = [
    "Hey?",
    "Wake up",
    "The time isn't right yet",
    "Emm...",
    "Can I know more about you?",
    "Emm... okay",
]

code = f"""
<div id="type_box" style="background:#222;padding:24px;border‑radius:12px;color:white;text‑align:center;font‑size:18px;min‑height:120px;"></div>
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
