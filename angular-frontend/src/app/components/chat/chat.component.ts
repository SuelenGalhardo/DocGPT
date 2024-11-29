import { Component } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})
export class ChatComponent {
  messages: { text: string; sender: 'user' | 'system' }[] = [];
  userInput: string = '';
  selectedFile: File | null = null;

  constructor(private apiService: ApiService) {}

  // Función para enviar mensajes al chat
  sendMessage() {
    if (!this.userInput.trim()) return;

    this.messages.push({ text: this.userInput, sender: 'user' });

    this.apiService.interactWithChat(this.userInput).subscribe({
      next: (res) => {
        this.messages.push({ text: res.response, sender: 'system' });
      },
      error: () => {
        this.messages.push({ text: 'Error al procesar tu solicitud.', sender: 'system' });
      },
    });

    this.userInput = '';
  }

  // Función para abrir el cargador de archivos
  openFileUploader() {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.txt';
    fileInput.onchange = (event: any) => {
      this.selectedFile = event.target.files[0];
     // this.uploadFile();
    };
    fileInput.click();
  }

  
 

  // Función para traducir mensajes
  translateMessage() {
    if (!this.userInput.trim()) return;

    this.messages.push({ text: `Traduciendo: ${this.userInput}`, sender: 'user' });

    this.apiService.translateText(this.userInput, 'es').subscribe({
      next: (res) => {
        this.messages.push({ text: res.translation, sender: 'system' });
      },
      error: () => {
        this.messages.push({ text: 'Error al traducir el mensaje.', sender: 'system' });
      },
    });

    this.userInput = '';
  }

  // Función para resumir mensajes
  summarizeMessage() {
    if (!this.userInput.trim()) return;

    this.messages.push({ text: `Resumiendo: ${this.userInput}`, sender: 'user' });

    this.apiService.summarizeText(this.userInput).subscribe({
      next: (res) => {
        this.messages.push({ text: res.summary, sender: 'system' });
      },
      error: () => {
        this.messages.push({ text: 'Error al resumir el mensaje.', sender: 'system' });
      },
    });

    this.userInput = '';
  }

  // Función para modificar texto
  modifyMessage() {
    if (!this.userInput.trim()) return;

    const modifications = { uppercase: true }; // Ejemplo de modificaciones

    this.messages.push({ text: `Modificando: ${this.userInput}`, sender: 'user' });

    this.apiService.modifyText(this.userInput, modifications).subscribe({
      next: (res) => {
        this.messages.push({ text: res.modified_text, sender: 'system' });
      },
      error: () => {
        this.messages.push({ text: 'Error al modificar el texto.', sender: 'system' });
      },
    });

    this.userInput = '';
  }

  // Función para subir y traducir un archivo
  uploadAndTranslateFile() {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.txt';
    fileInput.onchange = (event: any) => {
      const selectedFile = event.target.files[0];
      const targetLanguage = 'es'; // Puedes permitir al usuario seleccionar esto

      this.messages.push({ text: `Traduciendo archivo: ${selectedFile.name}`, sender: 'user' });

      this.apiService.uploadAndTranslate(selectedFile, targetLanguage).subscribe({
        next: (res) => {
          this.messages.push({ text: `Traducción: ${res.translation}`, sender: 'system' });
        },
        error: () => {
          this.messages.push({ text: 'Error al traducir el archivo.', sender: 'system' });
        },
      });
    };
    fileInput.click();
  }
}
