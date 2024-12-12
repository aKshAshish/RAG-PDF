import { BASE_URL } from "../utils/constants";

export const getReply = async (query, index) => {
    const url = `${BASE_URL}/chat`;
    const headers = new Headers();
    headers.append("content-type", "application/json");
    headers.append("accept", "application/json");

    const opions = {
        method: "POST",
        body: JSON.stringify({ query: query, index: index }),
        headers: headers,
    };
    return await fetch(url, opions);
};
