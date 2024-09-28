import {Component} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AccountsService} from "../accounts.service";
import {HttpClient} from "@angular/common/http";
import {BACKEND_IP} from "../../globals";
import {forkJoin} from "rxjs";

@Component({
  selector: 'app-send-message',
  standalone: true,
  imports: [
    FormsModule,
    ReactiveFormsModule
  ],
  templateUrl: './send-message.component.html',
  styleUrl: './send-message.component.css'
})
export class SendMessageComponent {
  message: string = '';
  delay: number = 0;
  channels: File | null = null;

  constructor(private accountsService: AccountsService, private http: HttpClient) {
  }

  onFileChange(event: any) {
    this.channels = event.target.files[0];
  }

  sendMessage() {
    const selectedAccounts = this.accountsService.accounts.filter(account => account.selected);
    const formData = new FormData();
    selectedAccounts.forEach(account => {
      formData.append('telegram_accounts', account.telegram_id.toString());
    });
    formData.append('message', this.message);
    formData.append('delay', this.delay.toString());
    if (this.channels) {
      formData.append('channels', this.channels);
    }

    this.http.post(BACKEND_IP + '/api/send-message/', formData).subscribe(() => {
      window.location.reload();
    });
  }
}
