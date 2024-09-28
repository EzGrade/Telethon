import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { HttpClient } from "@angular/common/http";
import { AccountsService } from "../accounts.service";
import { BACKEND_IP } from "../../globals";

@Component({
  selector: 'app-join-channels',
  standalone: true,
  imports: [
    FormsModule,
    ReactiveFormsModule
  ],
  templateUrl: './join-channels.component.html',
  styleUrl: './join-channels.component.css'
})
export class JoinChannelsComponent {
  delay: string = '';
  channels: File | null = null;

  constructor(private http: HttpClient, private accountsService: AccountsService) {}

  onFileChange(event: any) {
    this.channels = event.target.files[0];
  }

  joinChannels() {
    const selectedAccounts = this.accountsService.accounts.filter(account => account.selected);
    const formData = new FormData();
    selectedAccounts.forEach(account => {
      formData.append('telegram_accounts', account.telegram_id.toString());
    });
    formData.append('delay', this.delay);
    if (this.channels) {
      formData.append('channels', this.channels);
    }

    this.http.post(BACKEND_IP + '/api/subscribe-channels/', formData).subscribe(() => {
      window.location.reload();
    });
  }
}
