import chatLogo from "../assets/img/chatLogo.png";

const ReplyBox = ({ reply }) => {
    return (
        <div className="reply-box">
            <div className="chat-logo">
                <img src={chatLogo}></img>
            </div>
            <p>{reply}</p>
        </div>
    );
};

export default ReplyBox;
