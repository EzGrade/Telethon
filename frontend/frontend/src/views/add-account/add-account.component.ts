import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpClient} from '@angular/common/http';
import {BACKEND_IP} from '../../globals';

@Component({
  selector: 'app-add-account',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './add-account.component.html',
  styleUrl: './add-account.component.css'
})
export class AddAccountComponent {
  apiId: string = '';
  apiHash: string = '';
  sessionFile: File | null = null;

  constructor(private http: HttpClient) {
  }

  onFileChange(event: any) {
    this.sessionFile = event.target.files[0];
  }

  addAccount() {
    const formData = new FormData();
    formData.append('api_id', this.apiId);
    formData.append('api_hash', this.apiHash);
    if (this.sessionFile) {
      formData.append('session_file', this.sessionFile);
    }

    this.http.post(BACKEND_IP + '/api/telegram-accounts/', formData, { observe: 'response' }).subscribe(response => {
      if (response.status === 201) {
        window.location.reload();
      }
    }, error => {
      alert('Error adding account: ' + error);
    });
  }
}
