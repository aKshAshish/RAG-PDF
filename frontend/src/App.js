import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import ChatBox from "./components/ChatBox";

import "./index.css";

const App = () => {
    return (
        <div id="main">
            <Sidebar />
            <div id="chat-container">
                <Header />
                <ChatBox />
            </div>
        </div>
    );
};

export default App;
