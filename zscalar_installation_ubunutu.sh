#!/bin/bash

# Step 1: Copy the Zscaler root certificates from the Downloads folder
cd ~/Downloads
cp ZscalerRootCerts.zip /tmp/

# Step 2: Extract the certificates from the downloaded ZIP file
cd /tmp
unzip ZscalerRootCerts.zip

# Step 3: Copy the extracted certificate to the /usr/local/share/ca-certificates folder
cd /tmp/ZscalerRootCerts

# Copy the .cer file
sudo cp ZscalerRootCertificate-2048-SHA256.cer /usr/local/share/ca-certificates/

# Copy the .crt file
sudo cp ZscalerRootCertificate-2048-SHA256.crt /usr/local/share/ca-certificates/

# Step 4: Update the certificate list
sudo update-ca-certificates

# Validation: Check if the certificate is successfully updated
ls /etc/ssl/certs | grep ZscalerRootCertificate-2048-SHA256.pem

# Step 5: Copy the Zscaler client installer from the Downloads folder
cd ~/Downloads
cp Zscaler-linux-1.1.0.24-installer.zip /tmp/

# Step 6: Extract the installation file from the downloaded ZIP file
cd /tmp
unzip Zscaler-linux-1.1.0.24-installer.zip

# Step 7: Make the extracted .run file executable
cd /tmp
chmod +x Zscaler-linux-1.1.0.24-installer.run

# Step 8: Install ZPA client via terminal
sudo ./Zscaler-linux-1.1.0.24-installer.run --cloudName zscalertwo

# Step 9: Follow prompts to complete installation





# The Zscaler configuration code I provided earlier
  environment.systemPackages = [
    # Install Unzip to extract the certificates and Zscaler installer
    lib.package "unzip"

    # Add the Zscaler root certificates to the system's trusted CA certificates
    (let
      zscalerCertPath = "/etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem";
      zscalerCertSource = /path/to/ZscalerRootCertificate-2048-SHA256.cer; # Replace with the actual path
    in
    lib.overrideDerivation (oldAttrs: {
      name = "zscaler-root-certificate";
      src = null;
      installPhase = ''
        mkdir -p $out/etc/ssl/certs
        cp ${zscalerCertSource} $out/etc/ssl/certs/
        update-ca-certificates
      '';
    }))
  ];

  # Create a symbolic link to the Zscaler certificate
  environment.etc."ssl/certs/ZscalerRootCertificate-2048-SHA256.pem".source = "/etc/ssl/certs/ZscalerRootCertificate-2048-SHA256.pem";

  # Define a custom environment variable to set the cloudName
  environment.variables = {
    ZSCALER_CLOUD_NAME = "zscalertwo";
  };

  # Install Zscaler client via terminal
  systemd.services.zscaler = {
    description = "Zscaler Client Installation";
    wantedBy = [ "multi-user.target" ];
    after = [ "network.target" ];
    script = ''
      # Step 1: Copy the Zscaler root certificates
      cp /path/to/ZscalerRootCertificate-2048-SHA256.cer /etc/ssl/certs/
      cp /path/to/ZscalerRootCertificate-2048-SHA256.crt /etc/ssl/certs/
      update-ca-certificates

      # Step 2: Copy the Zscaler client installer
      cp /path/to/Zscaler-linux-1.1.0.24-installer.zip /tmp/

      # Step 3: Extract the installation file
      unzip /tmp/Zscaler-linux-1.1.0.24-installer.zip -d /tmp

      # Step 4: Make the installer executable
      chmod +x /tmp/Zscaler-linux-1.1.0.24-installer.run

      # Step 5: Install ZPA client
      /tmp/Zscaler-linux-1.1.0.24-installer.run --cloudName $ZSCALER_CLOUD_NAME
    '';
  };

