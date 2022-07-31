const API = {
    GetChatbotResponse: async (message) => {
        return new Promise(function (resolve, reject) {
            setTimeout(function () {
                //if (message === "hi") resolve("Welcome to chatbot!");
                fetch("http://localhost:8000/api/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ message }),
                })
                    .then((res) => res.json())
                    .then((replyMessage) => {
                        resolve(replyMessage.message);
                    })
                    .catch((err) => {
                        resolve("Something went wrong...");
                    });
            }, 2000);
        });
    },
};

export default API;
