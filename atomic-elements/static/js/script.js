const detailBox = document.getElementById("hover-details");
const symbolText = document.getElementById("detail-symbol");
const nameText = document.getElementById("detail-name");
const numberText = document.getElementById("detail-number");
const categoryText = document.getElementById("detail-category");
const weightText = document.getElementById("detail-weight");    
const discoveredByText = document.getElementById("detail-db");

document.querySelectorAll('.element-block').forEach(elem => {
    elem.addEventListener('mousemove', e => {
        const symbol = elem.dataset.symbol;
        const name = elem.dataset.name;
        const number = elem.dataset.number;
        const category = elem.dataset.category;
        const weight = elem.dataset.weight;
        const db = elem.dataset.db;
       

        symbolText.textContent = `Symbol: ${symbol}`;
        nameText.textContent = `Name: ${name}`;
        numberText.textContent = `Atomic Number: ${number}`;
        categoryText.textContent = `Category: ${category}`;
        weightText.textContent = `Atomic Mass: ${weight}`;
        discoveredByText.textContent = `Discovered By: ${db}`;
       

        detailBox.style.top = `${e.pageY + 10}px`;
        detailBox.style.left = `${e.pageX + 10}px`;
        detailBox.style.display = 'block';
    });

    elem.addEventListener('mouseleave', () => {
        detailBox.style.display = 'none';
    });

    elem.addEventListener('click', () => {
        const url = elem.dataset.url;
        if (url){
            window.open(url, '_blank');
        }
    });
});
