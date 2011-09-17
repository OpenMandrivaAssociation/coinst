%define debug_package %{nil}
%define name coinst
%define versionbase 1.0
#define releasecandidate rc5
%define release 3
#define versioncomplete %{versionbase}-%{releasecandidate}
%define versioncomplete %{versionbase}

Name:           %{name}
Version:        %{versionbase}
Release:        %{release}
Summary:        Coinstallability kernels for GNU/Linux distributions
Group:          Development/C
License:        GPLv2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://coinst.irill.org/
Source0:	http://www.pps.jussieu.fr/~vouillon/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:	ocaml-js-devel
BuildRequires:  ocaml-cairo-devel
BuildRequires:  ocaml-lablgtk2-devel

%global __ocaml_requires_opts -i Ast_c -i Token_c -i Type_cocci -i Ast_cocci -i Common -i Oassocb -i ANSITerminal -i Oseti -i Sexplib -i Oassoch -i Setb -i Oassoc_buffer -i Ograph2way -i SetPt -i Mapb -i Dumper -i Osetb -i Flag


%description
COINST reads the metadata of a GNU/Linux distribution (both RPM and DEB formats
are supported), and computes the co-installability kernel, which is orders of
magnitudes smaller than the original component graph, and yet contains all the
information necessary to identify components which are not co-installable. The
table below, extracted from the article, enumerate the number of packages,
dependencies and conflicts in the input and the output of the tool. 


%package viewer
Summary:        GTK Viewer for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}


%description viewer
The %{name}-examples package contains examples for %{name}.


%package webviewer
Summary:        Web/JS Viewer for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}


%description webviewer
The %{name}-examples package contains examples for %{name}.


%files
%{_bindir}/%{name}

%files viewer
%{_bindir}/%{name}_viewer
%{_bindir}/%{name}_converter

%files webviewer
%{_bindir}/jsviewer.byte
%{_datadir}/%{name}/*

%prep
%setup -q -n %{name}-%{versioncomplete}


%build
make

pushd viewer
make
popd

%install
%{__install} -m0755 -D %{name} %{buildroot}%{_bindir}/%{name}

pushd viewer
%{__install} -m0755 -D jsviewer.byte %{buildroot}%{_bindir}/jsviewer.byte
%{__install} -m0755 -D coinst_viewer %{buildroot}%{_bindir}/coinst_viewer
%{__install} -m0755 -D coinst_converter %{buildroot}%{_bindir}/coinst_converter

%{__install} -m0644 -D jsviewer.js %{buildroot}%{_datadir}/%{name}/jsviewer.js
%{__install} -m0644 -D index.html %{buildroot}%{_datadir}/%{name}/index.html
popd
