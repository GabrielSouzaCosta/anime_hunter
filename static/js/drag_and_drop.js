const rows = document.querySelectorAll('.items');
let animes = document.getElementById('items-tier');
let removeAnimes = document.getElementById('remove-items');

const onDragOver = (event) => {
    event.preventDefault();
}

const onDrop = (event) => {
    event.preventDefault();
    if (event.target.tagName == 'DIV' && event.target.classList.contains('items')) {
        const draggedCardId = event.dataTransfer.getData('id');
        const draggedCard = document.getElementById(draggedCardId);
        (event.target.id !== "drag-board") ?
        draggedCard.id = `${draggedCardId.split('-tier-')[0]}-tier-${event.target.id}`
        :
        draggedCard.id = `${draggedCardId.split('-tier-')[0]}-tier-none`

        console.log(draggedCard)
        draggedCard.style.visibility = 'visible';
        event.target.appendChild(draggedCard);
        if (event.target.id === "drag-board" && !removeAnimes.value.includes(draggedCard.id)) {
            if (removeAnimes.value === "") {
                removeAnimes.value += draggedCard.id;
            } else {
                removeAnimes.value += ` ${draggedCard.id}`;
            }
            animes.value = animes.value.replace(toString(draggedCard.id), " ");
        } else if (event.target.id === "drag-board") {
            animes.value = animes.value.replace(draggedCard.id, " ");
        } else if (animes.value === "") {
            animes.value = draggedCard.id;
        } else if (!animes.value.includes(draggedCard.id)) {
            animes.value += ` ${draggedCard.id}`;
        }
        console.log(animes.value + '\n' + removeAnimes.value)
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    rows.forEach((row) => {
        row.ondragover = onDragOver;
        row.ondrop = onDrop;
    })
})
