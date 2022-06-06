const rows = document.querySelectorAll('.items');
let animes = document.getElementById('items-tier');
let removeAnimes = document.getElementById('remove-items');

const onDragOver = (event) => {
    event.preventDefault();
}

const onDrop = (event) => {
    event.preventDefault();
    console.log(event.target)
    if (event.target.tagName == 'DIV' && event.target.classList.contains('items')) {
        const draggedCardId = event.dataTransfer.getData('id');
        const draggedCard = document.getElementById(draggedCardId);
        draggedCard.style.visibility = 'visible';
        event.target.appendChild(draggedCard);
        if (event.target.id === "drag-board" && !removeAnimes.value.includes(draggedCardId)) {
            if (removeAnimes.value === "") {
                removeAnimes.value += draggedCardId;
            } else {
                removeAnimes.value += ` ${draggedCardId}`;
            }
            animes.value = animes.value.replace(toString(draggedCardId), " ");
        } else if (event.target.id === "drag-board") {
            animes.value = animes.value.replace(draggedCardId, " ");
        } else if (animes.value === "") {
            animes.value += draggedCardId;
        } else if (!animes.value.includes(draggedCardId)) {
            animes.value += ` ${draggedCardId}`;
        }
        console.log(animes.value)
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    rows.forEach((row) => {
        row.ondragover = onDragOver;
        row.ondrop = onDrop;
    })
})
