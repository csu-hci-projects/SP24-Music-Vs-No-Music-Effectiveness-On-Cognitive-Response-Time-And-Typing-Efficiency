1. Install Xcode
If you don't have Xcode installed, download and install it from the Mac App Store or from the Apple Developer website.
2. Install openFrameworks
Download the latest version of openFrameworks from the openFrameworks website.
Follow the installation instructions provided on the website to set up openFrameworks on your system.
3. Clone the EyeWriter Project
Clone the EyeWriter project repository from GitHub:
git clone https://github.com/eyewriter/eyewriter.git
4. Update Project Settings
a. SDK and Deployment Target
Open the EyeWriter Xcode project (RemoteEyeTracker.xcodeproj) in Xcode.
In the project navigator, select the project file (RemoteEyeTracker).
Under "Build Settings," locate the "Base SDK" and "Deployment Target" settings.
Set the "Base SDK" to the latest macOS SDK available in Xcode.
Update the "Deployment Target" to match your current macOS version.
b. Valid Architectures
Still in the "Build Settings," search for "Valid Architectures" (VALID_ARCHS).
Replace the value with x86_64 to compile for modern Macs.
c. Header Search Paths
Navigate to "Build Settings" and search for "Header Search Paths" (HEADER_SEARCH_PATHS).
Add the path to the openFrameworks headers directory. For example:
/path/to/openFrameworks/libs
5. Update Code and Dependencies
Update Libraries: Ensure any external dependencies (like the GNU Scientific Library) are updated and compatible with your macOS version.
Fix Deprecated Code: Update any deprecated code or functions used in the EyeWriter project to match modern standards.
6. Build and Run
Ensure your PS3 eye camera drivers (Macam) and Arduino software are correctly installed.
Connect your Arduino board and upload the required sketch for the PS eye camera (StrobeEye.pde).
Build and run the EyeWriter project in Xcode (Product > Build).
