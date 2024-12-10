import { BASE_URL } from "../utils/constants";

export const uploadFile = async (file) => {
    if (file.type !== "application/pdf") {
        alert("Only PDF documents are allowed. Please select a valid document.");
        return;
    }
    const url = `${BASE_URL}/upload`;

    const formData = new FormData();
    formData.append("file", file);

    const options = {
        method: "POST",
        body: formData,
        redirect: "follow",
    };

    return await fetch(url, options);
};
