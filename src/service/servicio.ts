// service.ts

const API_ENDPOINT = 'https://www.pythonanywhere.com/user/kevinkiwi/shares/858437f206ea4e1d8f0f5a33a9d07498/send_data';  

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
