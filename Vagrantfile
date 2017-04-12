Vagrant.configure("2") do |config|
    config.vm.hostname = "ussdsimulator"
    config.vm.network :private_network, ip: "10.0.0.16"
    config.vm.box = "ubuntu/trusty64"
    config.vm.provision :shell, :path => "devops/bootstrap.sh"
end