import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // Método para interactuar con el endpoint de chat
  interactWithChat(text: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/chat`, { text });
  }

 

  // Método para traducir texto
  translateText(text: string, targetLanguage: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/translate`, { text, target_language: targetLanguage });
  }

  // Método para resumir texto
  summarizeText(text: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/summarize`, { text });
  }

  // Método para modificar texto
  modifyText(text: string, modifications: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/modify`, { text, modifications });
  }

  // Método para subir un archivo y traducirlo
  uploadAndTranslate(file: File, targetLanguage: string): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('target_language', targetLanguage);
    return this.http.post(`${this.apiUrl}/upload_and_translate`, formData);
  }
}
