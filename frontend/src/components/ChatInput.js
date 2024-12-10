const ChatInput = ({ chatText, setChatText }) => {
    const handleInput = (e) => {
        const textarea = e.target;
        textarea.style.height = "auto"; // Reset height
        textarea.style.height = `${textarea.scrollHeight}px`; // Adjust to content
        setChatText(textarea.value);
    };

    return (
        <textarea value={chatText} onChange={handleInput} placeholder="Ask anything..." rows={1} />
    );
};

export default ChatInput;
