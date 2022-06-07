const cards = document.querySelectorAll('.anime-card');
const labels = document.querySelectorAll('.tier-label');
const labelsInputForm = document.getElementById('tier-labels');

const onDragStart = (event) => {
    event.dataTransfer.setData('id', event.target.id);
    setTimeout(() => {
        event.target.style.visibility = 'hidden';
    }, 60)
}

const onDragEnd = (event) => {
    event.target.style.visibility = 'visible';
}

const handleLabelChange = (event) => {
    labelsInputForm.value = ""
    labels.forEach((v) => {
        if (v.id == event.target.id) {
            v.value = event.target.value;
        }
        (labelsInputForm.value === "") ?
        labelsInputForm.value += `${v.id}-${v.value}`
        :
        labelsInputForm.value += `,${v.id}-${v.value}`
    })
    console.log(labelsInputForm);
}

cards.forEach((card) => {
    card.ondragstart = onDragStart;
    card.ondragend = onDragEnd;
})

document.addEventListener('DOMContentLoaded', (event) => {
    labels.forEach((label) => {
        (labelsInputForm.value === "") ?
        labelsInputForm.value += `${label.id}-${label.value}` 
        :
        labelsInputForm.value += `,${label.id}-${label.value}`
        label.onchange = handleLabelChange;
    })
})
