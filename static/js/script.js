cardFlyers = document.querySelectorAll('.card-flyer');
hiddenCards = document.querySelectorAll('.hidden-card');


onMouseEnter = (event) => {
    event.target.querySelector('.hidden-card').style.visibility = 'visible';
}

onMouseLeave = (event) => {
    event.target.querySelector('.hidden-card').style.visibility = 'hidden';
}

document.addEventListener('DOMContentLoaded', (event) => {
    cardFlyers.forEach((card) => {
        card.onmouseenter = onMouseEnter;
        card.onmouseleave = onMouseLeave;
    })
})

