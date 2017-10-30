#!/usr/bin/env bash

echo "Setting up build";
export VERSION="1.0";

echo "Zipping";
zip -r9 SwiftDark.zip colors.tdesktop-theme swiftdark.png;

echo "Renaming"

mv SwiftDark.zip SwiftDark_v${VERSION}.tdesktop-theme;
