import {Routes} from '@angular/router';
import {AddAccountComponent} from "../views/add-account/add-account.component";
import {JoinChannelsComponent} from "../views/join-channels/join-channels.component";
import {SendMessageComponent} from "../views/send-message/send-message.component";
import {RemoveAccountComponent} from "../views/remove-account/remove-account.component";

export const routes: Routes = [
  {
    "path": "add-account",
    "component": AddAccountComponent
  },
  {
    "path": "send-message",
    "component": SendMessageComponent
  },
  {
    "path": "join-channels",
    "component": JoinChannelsComponent
  },
  {
    "path": "remove-account",
    "component": RemoveAccountComponent
  }
];
