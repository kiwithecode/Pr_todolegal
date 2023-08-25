// service.ts

const API_ENDPOINT = 'http://127.0.0.1:5000/send_data';  

export async function sendData(name: string, file: File): Promise<any> {
  const formData = new FormData();
  formData.append('name', name);
  formData.append('file', file);

  const response = await fetch(API_ENDPOINT, {
    method: 'POST',
    body: formData,
  });

  return await response.json();
}
