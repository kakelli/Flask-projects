document.addEventListener('DOMContentLoaded', () => {
    const quizData = window.quizData;
    const resultsDiv = document.getElementById('results');

    quizData.forEach((q, index) => {
        const isCorrect = q.userAnswer.trim().toUpperCase() === q.correctAnswer.trim().toUpperCase();
        const block = document.createElement('div');
        block.className = 'question-block';

        block.innerHTML = `
            <h3> Question ${index + 1} </h3>
            <p><strong>Your Answer: </strong><span class="${isCorrect ? 'correct':'incorrect'}">{q.userAnswer}</span></p>
            `;
        resultsDiv.appendChild(block);
    });
})