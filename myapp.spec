Name:           myapp
Version:        1.0
Release:        1%{?dist}
Summary:        My sample application

License:        GPL
URL:            https://github.com/alexandra-kononenko/study_repository
Source0:        myscript.sh

BuildArch:      noarch

%description
Script that will calculate the amount of files excluding directories and links in /etc directory

%prep


%build


%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/myscript.sh

%files
/usr/local/bin/myscript.sh

%changelog
