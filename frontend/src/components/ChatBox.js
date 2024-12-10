import { useEffect, useState, useRef } from "react";

import ChatInput from "./ChatInput";
import QueryBox from "./QueryBox";
import ReplyBox from "./ReplyBox";

import { ChatType } from "../utils/constants";
import { getReply } from "../services/chat.service";
import { uploadFile } from "../services/document.service";

const ChatBox = () => {
    const [chatText, setChatText] = useState("");
    const [chats, setChats] = useState([]);
    const [isChatDisabled, setIsChatDisabled] = useState(true);
    const [isWaiting, setIsWaiting] = useState(false);
    const fileInputRef = useRef(null);

    const handleChatInput = () => {
        setIsWaiting(true); // Disable the chat button while getting the reply
        const query = chatText;
        setChatText("");
        newChats = [...chats, { type: ChatType.QUERY, text: query }];
        setChats(newChats);
        const reply = getReply(query);
        setChats([...newChats, { type: ChatType.REPLY, text: reply }]);
        setIsWaiting(false); // Enable the chat button.
    };

    useEffect(() => {
        // Disable the chat button if fetching reply or there is no query
        setIsChatDisabled(isWaiting || !chatText);
    }, [chatText, isWaiting]);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (!file) {
            return;
        }
        // Upload File to server
        uploadFile(file)
            .then((response) => {
                if (response && response.status === 200) {
                    alert(`File ${file.name} is uploaded successfully.`);
                }
            })
            .catch((err) => {
                alert(`Error: ${err}`);
            });
    };

    return (
        <div id="chat-box">
            <div id="chat-disp-area">
                {chats.map((chat, idx) => {
                    if (chat.type === ChatType.QUERY) {
                        return <QueryBox key={idx} query={chat.text} />;
                    }
                    return <ReplyBox key={idx} reply={chat.text} />;
                })}
            </div>
            <div id="chat-input-box">
                <ChatInput chatText={chatText} setChatText={setChatText} />
                <div className="btn-container">
                    <button onClick={() => fileInputRef.current.click()}>
                        <i className="material-icons">attach_file</i>
                        <input
                            onChange={handleFileChange}
                            ref={fileInputRef}
                            type="file"
                            style={{ display: "none" }}
                        ></input>
                    </button>
                    <button onClick={handleChatInput} disabled={isChatDisabled}>
                        <i className="material-icons">arrow_forward</i>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatBox;
