import {Component} from '@angular/core';
import {Router, RouterLink} from "@angular/router";
import {NgClass} from "@angular/common";

@Component({
  selector: 'app-action-selector',
  standalone: true,
  imports: [
    RouterLink,
    NgClass
  ],
  templateUrl: './action-selector.component.html',
  styleUrl: './action-selector.component.css'
})
export class ActionSelectorComponent {
  constructor(private router: Router) {
  }

  isAddAccountRoute(): boolean {
    return this.router.url === '/add-account';
  }

  isSendMessagesRoute(): boolean {
    return this.router.url === '/send-message';
  }

  isJoinChannelsRoute(): boolean {
    return this.router.url === '/join-channels';
  }

  isRemoveAccountRoute(): boolean {
    return this.router.url === '/remove-account';
  }
}
