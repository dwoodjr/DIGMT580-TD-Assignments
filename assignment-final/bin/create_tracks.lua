reaper.ShowMessageBox('Type the number of tracks to create. Insert an integer between 1 - 16.','Number of Midi Channels: Help:',0)

local continue, midi_channels = reaper.GetUserInputs('Insert Number of MIDI Channels', 1, 'MIDI Channel Number: extrawidth=50', '')
    reaper.MB(midi_channels,'Number of Tracks Created',0)

if not continue or midi_channels == '' then return end

local track_cnt = midi_channels

--[ Variables for automatic L to R pan
start_val = -1.0
end_val = track_cnt
step = (end_val - start_val)/track_cnt
--]

--[ Variables for automatic L to R pan
midi_id = 4096
midi_device = 64
--]

--[ Variables for automatic L to R pan
local effects = {"LABS", "ReaSynth", "ReaSynDr"}
--]

for i = 0, track_cnt-1 do

  --insert tracks at index
  reaper.InsertTrackAtIndex(track_cnt-1, true)
  
  --get all tracks
  tr = reaper.GetTrack(0, i)
  
  --pan from L to R
  val_get = reaper.GetMediaTrackInfo_Value(tr, "D_PAN")
  if 
    tonumber(track_cnt) < 2 then pan_val = 0
  else
    pan_val = start_val+(2.0/((track_cnt-1))*(i))
  end
  reaper.SetMediaTrackInfo_Value(tr, "D_PAN", pan_val)
  
  --set Midi input decive
  midi_chan = i+1 --(i+1 * (track_cnt-1))-1
  reaper.SetMediaTrackInfo_Value(tr, "I_RECINPUT", midi_id + midi_chan + midi_device)
  
  --arm tracks
  reaper.SetMediaTrackInfo_Value(tr, "I_RECARM", 1)
  
  --add FX to track
  for _, effect in ipairs(effects) do
    local index = reaper.TrackFX_AddByName(tr, effect, false, 1)
    reaper.TrackFX_SetOpen(tr, index, not reaper.TrackFX_GetOpen(tr, index))
    reaper.TrackFX_SetEnabled(tr, index, true)
  end
     
end

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

