async function summarizeText() {
    const inputText = document.getElementById('input-text').value;
    const loadingIndicator = document.getElementById('loading');
    const summaryOutput = document.getElementById('summary-output');

    // Show loading indicator
    loadingIndicator.style.display = 'block';
    summaryOutput.innerText = '';

    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    });

    const result = await response.json();

    // Hide loading indicator
    loadingIndicator.style.display = 'none';
    summaryOutput.innerText = result.summary;
}
