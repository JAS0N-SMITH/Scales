# Scales
This project is a Musical Scale Machine that helps musicians work with different musical scales and chord progressions. Here's a breakdown of its main features:

Scale Generation

Uses the Scale_Options dictionary to define various musical scales including:
Major and Natural Minor scales
Pentatonic scales (Major and Minor)
Blues Scale
Various modes (Mixolydian, Lydian, Locrian, Dorian, Phrygian)
Each scale is defined by its number of degrees and interval pattern
Note Management

Uses the Note class to represent musical notes
Supports all 12 notes: C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B
Can reorganize notes based on a chosen tonic (starting note)
Chord Progression Generation

The Chord_Progression class generates common chord progressions based on the scale type
For Major scales:
I - IV - V - I
I - V - IV - I
I - ii - V - I
For Minor scales:
i - iv - v - i
i - v - iv - i
i - ii° - v - i
User Interface

Command-line interface that allows users to:
Choose a tonic note
Select a scale type from the available options
View the resulting scale with degree symbols
See possible chord progressions for that scale
The program is used by running main.py, which presents a menu where users can input their desired tonic note and scale type, and then displays the resulting scale degrees and chord progressions.

There's also a known bug mentioned in the README.md where the C Lydian Mode uses Gb instead of the more musically correct F#.

TODO: 
<ol>
<li>Automate tests</li>
<li>Add scales and modes to the list of available patterns</li>
<li>Clean up objects and functions</li>
<li>Document code</li>
<li>Build Chord Objects</li>
<li>Build Chord Progression Objects</li>
<li>UI</li>
<li>Deployment</li>
</ol>
Bugs:
<dl>
<dt>C Lydian Mode uses Gb instead of F#</dt>
<dd>Because using F# would be proper</dd>
</dl>
