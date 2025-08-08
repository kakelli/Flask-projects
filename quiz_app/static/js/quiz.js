document.addEventListener('DOMContentLoaded', ()=>{
    const form = document.querySelector('form');
    const questions = document.querySelector('.question');

    form.addEventListener('submit', (e) => {
        let allAnswered = true;

        questions.forEach((q) => {
                const selected = q.querySelector('input[type="radio"]:checked');
                if (!selected){
                    allAnswered = false;
                    q.classList.add('unanswered');
                } else{
                    q.classList.remove('unanswered');
                }
        });

        if(!allAnswered){
            e.preventDefault();
            alert('Please answer all the questions before submitting')
        }
    })
})