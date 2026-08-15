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


function askQuickQuestion(question) {

    document.getElementById(
        "questionInput"
    ).value =
        question;


    sendQuestion();

}


function handleKeyPress(event) {

    if (
        event.key === "Enter"
    ) {

        sendQuestion();

    }

}


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
            ${text}
        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();

}


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


    message.innerHTML =
        `
        <div class="ai-message">
            🤖 <strong>College AI</strong>
            <br><br>
            ${text}
        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();

}


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
            🤖 <strong>College AI is thinking...</strong>
        </div>
        `;


    container.appendChild(
        message
    );


    scrollToBottom();


    return message;

}


function scrollToBottom() {

    const container =
        document.getElementById(
            "chatContainer"
        );


    container.scrollTop =
        container.scrollHeight;

}
