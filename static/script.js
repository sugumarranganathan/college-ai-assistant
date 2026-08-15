// --------------------------------------------------
// SEND QUESTION
// --------------------------------------------------

async function sendQuestion() {

    const input =
        document.getElementById(
            "questionInput"
        );

    const question =
        input.value.trim();


    if (!question) {
        return;
    }


    addUserMessage(
        question
    );


    input.value = "";


    const loadingMessage =
        addLoadingMessage();


    try {

        const response =
            await fetch(
                "/ask",
                {
                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({
                            question:
                                question
                        })
                }
            );


        const data =
            await response.json();


        loadingMessage.remove();


        addAIMessage(
            data.answer
        );

    }

    catch (error) {

        loadingMessage.remove();


        addAIMessage(
            "Sorry, something went wrong. Please try again."
        );

    }

}


// --------------------------------------------------
// QUICK QUESTIONS
// --------------------------------------------------

function askQuickQuestion(question) {

    document.getElementById(
        "questionInput"
    ).value =
        question;


    sendQuestion();

}


// --------------------------------------------------
// ENTER KEY
// --------------------------------------------------

function handleKeyPress(event) {

    if (
        event.key === "Enter"
    ) {

        sendQuestion();

    }

}


// --------------------------------------------------
// ESCAPE HTML
// --------------------------------------------------

function escapeHTML(text) {

    const div =
        document.createElement(
            "div"
        );


    div.textContent =
        text;


    return div.innerHTML;

}


// --------------------------------------------------
// ADD USER MESSAGE
// --------------------------------------------------

function addUserMessage(text) {

    const container =
        document.getElementById(
            "chatContainer"
        );


    const message =
        document.createElement(
            "div"
        );


    message.className =
        "message";


    message.innerHTML =
        `
        <div class="user-message">
            ${escapeHTML(text)}
        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();

}


// --------------------------------------------------
// FORMAT AI RESPONSE
// --------------------------------------------------

function formatAIResponse(text) {

    // --------------------------------------------------
    // ESCAPE HTML
    // --------------------------------------------------

    let formatted =
        escapeHTML(text);


    // --------------------------------------------------
    // NORMALIZE WINDOWS / LINUX LINE ENDINGS
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\r\n/g,
            "\n"
        );


    // --------------------------------------------------
    // REMOVE EXCESSIVE EMPTY LINES
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\n[ \t]*\n[ \t]*\n+/g,
            "\n\n"
        );


    // --------------------------------------------------
    // FIX NUMBER ON SEPARATE LINE
    //
    // BEFORE:
    //
    // 1
    //
    // **Eligibility Check**
    //
    // AFTER:
    //
    // 1. **Eligibility Check**
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /(^|\n)[ \t]*(\d+)[ \t]*\n+[ \t]*/g,
            "$1$2. "
        );


    // --------------------------------------------------
    // FIX 🔹 ON SEPARATE LINE
    //
    // BEFORE:
    //
    // 🔹
    //
    // Computer Science
    //
    // AFTER:
    //
    // 🔹 Computer Science
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /(^|\n)[ \t]*🔹[ \t]*\n+[ \t]*/g,
            "$1🔹 "
        );


    // --------------------------------------------------
    // FIX OTHER BULLETS ON SEPARATE LINE
    //
    // -
    // Content
    //
    // •
    // Content
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /(^|\n)[ \t]*[-•][ \t]*\n+[ \t]*/g,
            "$1• "
        );


    // --------------------------------------------------
    // CONVERT BOLD TEXT
    //
    // **Text**
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\*\*(.*?)\*\*/g,
            "<strong>$1</strong>"
        );


    // --------------------------------------------------
    // NUMBERED LIST CARDS
    //
    // 1. Content
    // 2. Content
    //
    // Each number and its complete content
    // become one beautiful card.
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /(^|\n)[ \t]*(\d+)\.[ \t]+([\s\S]*?)(?=\n[ \t]*\d+\.[ \t]+|\n\n|$)/g,
            function (
                match,
                lineStart,
                number,
                content
            ) {

                return `
<div class="ai-number-item">

    <div class="number-badge">
        ${number}
    </div>

    <div class="number-content">
        ${content.trim()}
    </div>

</div>
`;

            }
        );


    // --------------------------------------------------
    // BULLET LIST ITEMS
    //
    // 🔹 Computer Science
    // • Computer Science
    // - Computer Science
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /(^|\n)[ \t]*(🔹|•|-)[ \t]+(.*?)(?=\n|$)/g,
            function (
                match,
                lineStart,
                bullet,
                content
            ) {

                return `
<div class="ai-bullet-item">

    <span class="bullet-icon">
        🔹
    </span>

    <span class="bullet-content">
        ${content.trim()}
    </span>

</div>
`;

            }
        );


    // --------------------------------------------------
    // IMPORTANT / NOTE HIGHLIGHT
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\b(Important:|IMPORTANT:|Note:|NOTE:)/g,
            `<span class="important-text">💡 $1</span>`
        );


    // --------------------------------------------------
    // REMOVE EXTRA EMPTY LINES AGAIN
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\n{3,}/g,
            "\n\n"
        );


    // --------------------------------------------------
    // CONVERT REMAINING LINE BREAKS
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /\n/g,
            "<br>"
        );


    // --------------------------------------------------
    // CLEAN <br> BEFORE NUMBER CARDS
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /<br>\s*(<div class="ai-number-item">)/g,
            "$1"
        );


    // --------------------------------------------------
    // CLEAN <br> BEFORE BULLET ITEMS
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /<br>\s*(<div class="ai-bullet-item">)/g,
            "$1"
        );


    // --------------------------------------------------
    // CLEAN EXTRA <br> AFTER CARDS
    // --------------------------------------------------

    formatted =
        formatted.replace(
            /<\/div>\s*<br>\s*<br>/g,
            "</div>"
        );


    return formatted;

}


// --------------------------------------------------
// ADD AI MESSAGE
// --------------------------------------------------

function addAIMessage(text) {

    const container =
        document.getElementById(
            "chatContainer"
        );


    const message =
        document.createElement(
            "div"
        );


    message.className =
        "message";


    const formattedText =
        formatAIResponse(
            text
        );


    message.innerHTML =
        `
        <div class="ai-message">

            <div class="ai-header">

                <span class="ai-icon">
                    🤖
                </span>

                <strong>
                    College AI
                </strong>

                <span class="ai-status">
                    ✨ AI Response
                </span>

            </div>


            <div class="ai-response">

                ${formattedText}

            </div>

        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();

}


// --------------------------------------------------
// ADD LOADING MESSAGE
// --------------------------------------------------

function addLoadingMessage() {

    const container =
        document.getElementById(
            "chatContainer"
        );


    const message =
        document.createElement(
            "div"
        );


    message.className =
        "message loading";


    message.innerHTML =
        `
        <div class="ai-message">

            <div class="ai-header">

                <span class="ai-icon">
                    🤖
                </span>

                <strong>
                    College AI
                </strong>

            </div>


            <div class="thinking">

                <span>
                    Thinking
                </span>

                <span class="dot">
                    .
                </span>

                <span class="dot">
                    .
                </span>

                <span class="dot">
                    .
                </span>

            </div>

        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();


    return message;

}


// --------------------------------------------------
// SCROLL TO BOTTOM
// --------------------------------------------------

function scrollToBottom() {

    const container =
        document.getElementById(
            "chatContainer"
        );


    container.scrollTop =
        container.scrollHeight;

}