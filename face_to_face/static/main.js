var tip_h2 = document.getElementById("tipIndex")
var i = 0
function changeIndex() {
    const paragraph = document.createElement("p")
    if (i == 0) {
        x = "{{ tip_person[0] }}"
    } else if (i == 1) {
        x = "{{ tip_person[1] }}"
    } else if (i == 2) {
        x = "{{ tip_person[2] }}"
    } else if (i == 3) {
        x = "{{ tip_person[3] }}"
    } else if (i == 4) {
        x = "{{ tip_person[4] }}"
        i = 0
    }

    const text = document.createTextNode(x)
    paragraph.appendChild(text)

    tip_h2.innerHTML += `<br>${paragraph.innerHTML}`
    i += 1
}
