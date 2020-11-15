FROM microsoft/dotnet:1.0.0-preview2-sdk

WORKDIR /app

ADD src/Hello src/Hello

RUN dotnet restore -v minimal src/ \
    && dotnet publish -c Release -o ./ src/Hello/ \
    && rm -rf src/ $HOME/.nuget/

CMD dotnet Hello.dll
