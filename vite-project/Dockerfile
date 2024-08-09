# Dockerfile for React Frontend
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Install serve to serve the built React app
RUN npm install -g serve

# Expose the port the app will run on
EXPOSE 5000

# Command to run the React application with serve
CMD ["serve", "-s", "build", "-l", "5000"]
