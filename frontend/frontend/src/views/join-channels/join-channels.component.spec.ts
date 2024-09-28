import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JoinChannelsComponent } from './join-channels.component';

describe('JoinChannelsComponent', () => {
  let component: JoinChannelsComponent;
  let fixture: ComponentFixture<JoinChannelsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [JoinChannelsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(JoinChannelsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
